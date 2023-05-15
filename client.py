from io import BytesIO
from typing import TypeVar, Literal, Optional, Union
from urllib.parse import urlencode

import httpx

from .endpoint import ArcaeaUnlimitedAPIEndpoint as Endpoint
from .exception import ArcaeaUnlimitedAPIError
from .model import (
    BaseResponse,
    UserInfo, UserBest, UserBestsSession, UserBestsResult,
    SongList, SongInfo, SongAlias, SongRandom,
    DataUpdate, DataTheory, DataChallenge, DataCert
)

BaseResponse_T = TypeVar('BaseResponse_T', bound=BaseResponse)


def set_params(**kwargs): return {k: v for k, v in kwargs.items() if v is not None and k != 'self'}


class ArcaeaUnlimitedAPIClient:

    def __init__(
            self,
            api_entry: str,
            user_agent: str,
            token: str,
            proxies: Optional[str] = None,
            timeout: float = 15,
            retries: int = 0,
    ):
        self.api_entry = api_entry.removesuffix('/')
        self.user_agent = user_agent
        self.token = token.removeprefix('Bearer ')
        self.proxies = proxies
        self.timeout = timeout
        self.retries = retries
        self._headers = {'User-Agent': self.user_agent, 'Authorization': f'Bearer {self.token}'}

    def _get_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            proxies=self.proxies,
            timeout=self.timeout,
            transport=httpx.AsyncHTTPTransport(retries=self.retries) if self.retries else None
        )

    async def _aua_request_json(self, endpoint: str, params: dict, model: type[BaseResponse_T]) -> BaseResponse_T:
        async with self._get_client() as client:
            resp = await client.get(self.api_entry + endpoint, params=params, headers=self._headers)
            resp_as_model = model(**resp.json())

        if resp.status_code != 200:
            raise ArcaeaUnlimitedAPIError(resp_as_model.status, resp_as_model.message)

        return resp_as_model

    async def _aua_request_bytes(self, endpoint: str, params: dict) -> BytesIO:
        async with self._get_client() as client:
            resp = await client.get(self.api_entry + endpoint, params=params, headers=self._headers)

        if resp.status_code != 200:
            resp_as_model = BaseResponse(**resp.json())
            raise ArcaeaUnlimitedAPIError(resp_as_model.status, resp_as_model.message)

        return BytesIO(resp.content)

    async def get_user_info(
            self,
            user_name: Optional[str] = None,
            user_code: Optional[str] = None,
            recent: Optional[int] = None,
            withsonginfo: Optional[bool] = None
    ) -> UserInfo:
        """
        Get user info and recent score.

        :param user_name: user name or 9-digit user code, optional when usercode is not null, otherwise false
        :param user_code: 9-digit user code, optional when user is not null, otherwise false
        :param recent: (Optional) number, range 0-7. The number of recently played songs expected
        :param withsonginfo: (Optional) boolean. if true, will reply with songinfo
        """

        if not user_name and not user_code:
            raise ValueError('user and usercode cannot be both None')
        if recent and recent not in range(8):
            raise ValueError('recent must be in range 0-7')

        return await self._aua_request_json(Endpoint.User.info, set_params(**locals()), UserInfo)

    async def get_user_best(
            self,
            difficulty: Union[int, str],
            user_name: Optional[str] = None,
            user_code: Optional[str] = None,
            song_name: Optional[str] = None,
            songid: Optional[str] = None,
            with_recent: Optional[bool] = None,
            with_song_info: Optional[bool] = None
    ) -> UserBest:
        """
        Get user's best score of given chart.

        :param difficulty: accept format are 0/1/2/3 or pst/prs/ftr/byn or past/present/future/beyond
        :param user_name: user name or 9-digit user code, optional when usercode is not null, otherwise false
        :param user_code: 9-digit user code, optional when user is not null, otherwise false
        :param song_name: any song name for fuzzy querying, optional when songid is not null, otherwise false
        :param songid: sid in Arcaea songlist, optional when songname is not null, otherwise false
        :param with_recent: (Optional) boolean. if true, will reply with recent score
        :param with_song_info: (Optional) boolean. if true, will reply with songinfo
        """

        if not user_name and not user_code:
            raise ValueError('user and usercode cannot be both None')
        if not song_name and not songid:
            raise ValueError('songname and songid cannot be both None')
        if all((
                difficulty not in range(4),
                difficulty not in ('pst', 'prs', 'ftr', 'byn'),
                difficulty not in ('past', 'present', 'future', 'beyond')
        )):
            raise ValueError('difficulty must be in range 0-3 or pst/prs/ftr/byn or past/present/future/beyond')

        return await self._aua_request_json(Endpoint.User.best, set_params(**locals()), UserBest)

    async def get_user_bests_session(self, user_name: Optional[str] = None, user_code: Optional[str] = None) -> UserBestsSession:
        """
        Get user's bests query queue session.

        :param user_name: user name or 9-digit user code, optional when usercode is not null, otherwise false
        :param user_code: 9-digit user code, optional when user is not null, otherwise false
        """

        if not user_name and not user_code:
            raise ValueError('user and usercode cannot be both None')

        return await self._aua_request_json(Endpoint.User.bests_session, set_params(**locals()), UserBestsSession)

    async def get_user_bests_result(
            self,
            session_info: str,
            overflow: Optional[int] = None,
            with_recent: Optional[bool] = None,
            with_song_info: Optional[bool] = None
    ) -> UserBestsResult:
        """
        Get user's best 30 scores.

        Note: This api is cache-based and the results may not be real-time.

        :param session_info: session_info from `user/bests/session`
        :param overflow: (Optional) number, range 0-10. The number of the overflow records below the best30 minimum
        :param with_recent: (Optional) boolean. if true, will reply with recent_score
        :param with_song_info: (Optional) boolean. if true, will reply with songinfo
        """

        if overflow and overflow not in range(11):
            raise ValueError('overflow must be in range 0-10')

        return await self._aua_request_json(Endpoint.User.bests_result, set_params(**locals()), UserBestsResult)

    async def get_song_info(self, song_name: Optional[str] = None, song_id: Optional[str] = None) -> SongInfo:
        """
        Get song's all difficulty and its alias.

        :param song_name: any song name for fuzzy querying, optional when songid is not null, otherwise false
        :param song_id: sid in Arcaea songlist, optional when songname is not null, otherwise false
        """

        if not song_name and not song_id:
            raise ValueError('songname and songid cannot be both None')

        return await self._aua_request_json(Endpoint.Song.info, set_params(**locals()), SongInfo)

    async def get_song_list(self) -> SongList:
        """Get song list."""

        return await self._aua_request_json(Endpoint.Song.list, {}, SongList)

    async def get_song_alias(self, song_name: Optional[str] = None, song_id: Optional[str] = None) -> SongAlias:
        """
        Get song's alias.

        :param song_name: any song name for fuzzy querying, optional when songid is not null, otherwise false
        :param song_id: sid in Arcaea songlist, optional when songname is not null, otherwise false
        """

        if not song_name and not song_id:
            raise ValueError('songname and songid cannot be both None')

        return await self._aua_request_json(Endpoint.Song.alias, set_params(**locals()), SongAlias)

    async def get_song_random(
            self,
            start: Optional[int] = None,
            end: Optional[int] = None,
            with_song_info: Optional[bool] = None
    ):
        """
        Get a random song.

        Note: It is recommended to use song/list API as the local cache data source.

        :param start: (Optional) range of start (18 => 9, 21 => 10+)
        :param end: (Optional) range of end
        :param with_song_info: (Optional) boolean. if true, will reply with songinfo
        """

        return await self._aua_request_json(Endpoint.Song.random, set_params(**locals()), SongRandom)

    async def get_assets_icon(self, partner: int, awakened: Optional[bool] = None) -> BytesIO:
        """
        Get partner icon (PNG file).

        Note: It is not recommended to use this API frequently.

        :param partner: partner id
        :param awakened: (Optional) Boolean, partner is awakened
        """

        return await self._aua_request_bytes(Endpoint.Assets.icon, set_params(**locals()))

    async def get_assets_char(self, partner: int, awakened: Optional[bool] = None) -> BytesIO:
        """
        Get partner char (PNG file).

        Note: It is not recommended to use this API frequently.

        :param partner: partner id
        :param awakened: (Optional) Boolean, partner is awakened
        """

        return await self._aua_request_bytes(Endpoint.Assets.char, set_params(**locals()))

    async def get_assets_song(
            self,
            song_name: Optional[str] = None,
            song_id: Optional[str] = None,
            difficulty: Optional[Literal[3, 'byd', 'beyond']] = None,
            file: Optional[str] = None
    ):
        """
        Get song's cover (PNG file).

        Note: It is not recommended to use this API frequently.

        :param song_name: any song name for fuzzy querying, optional when songid is not null, otherwise false
        :param song_id: sid in Arcaea songlist, optional when songname is not null, otherwise false
        :param difficulty: (Optional) accept format are 3 or byn or beyond
        :param file: filename for special songs, such as stager_1 or melodyoflove_night,
            optional when songid or songname is not null, otherwise false
        """

        if not song_name and not song_id and not file:
            raise ValueError('songname, songid and file cannot be all None')
        if difficulty and difficulty not in (3, 'byn', 'beyond'):
            raise ValueError('difficulty only accept 3, byn or beyond')

        return await self._aua_request_bytes(Endpoint.Assets.song, set_params(**locals()))

    async def get_assets_aff(
            self,
            song_name: Optional[str] = None,
            song_id: Optional[str] = None,
            difficulty: Optional[Literal[3, 'byd', 'beyond']] = None,
    ):
        """
        Get song's aff (Arcaea chart file).

        Note: It is not recommended to use this API frequently, and this API only returns affs from the installation package.

        :param song_name: any song name for fuzzy querying, optional when song_id is not null, otherwise false
        :param song_id: sid in Arcaea songlist, optional when song_name is not null, otherwise false
        :param difficulty: (Optional) accept format are 3 or byn or beyond
        """

        if not song_name and not song_id:
            raise ValueError('song_name and song_id cannot be both None')
        if difficulty and difficulty not in (3, 'byn', 'beyond'):
            raise ValueError('difficulty only accept 3, byn or beyond')

        return await self._aua_request_bytes(Endpoint.Assets.aff, set_params(**locals()))

    async def get_assets_preview(
            self,
            song_name: Optional[str] = None,
            song_id: Optional[str] = None,
            difficulty: Union[str, int, None] = None,
            source: Literal['a2f', 'acr'] = 'a2f'
    ):
        """
        Get chart preview (PNG or WebP file).

        Note: It is not recommended to use this API frequently.

        :param song_name: any song name for fuzzy querying, optional when songid is not null, otherwise false
        :param song_id: sid in Arcaea songlist, optional when songname is not null, otherwise false
        :param difficulty: (Optional) 3 or byn or beyond (for a2f) or 0/1/2/3 (for acr)
        :param source: (Optional) from which source
        """

        if not song_name and not song_id:
            raise ValueError('songname and songid cannot be both None')

        # from Aff2Preview (https://github.com/Arcaea-Infinity/Aff2Preview)
        if source == 'a2f':
            if difficulty and all((
                    difficulty not in range(4),
                    difficulty not in ('pst', 'prs', 'ftr', 'byn'),
                    difficulty not in ('past', 'present', 'future', 'beyond')
            )):
                raise ValueError('Aff2Preview only accept difficulty in 0-3, pst/prs/ftr/byn or past/present/future/beyond')
            return await self._aua_request_bytes(Endpoint.Assets.preview, set_params(**locals()))

        # from ArcaeaChartRender (https://github.com/Arcaea-Infinity/ArcaeaChartRender)
        elif source == 'acr':
            if difficulty and difficulty not in range(4):
                raise ValueError('ArcaeaChartRender only accept difficulty in 0-3')
            if not song_id:
                raise ValueError('to use ArcaeaChartRender you must provide songid')
            async with self._get_client() as client:
                resp = await client.get(f'https://chart.arisa.moe/{song_id}/{difficulty}.webp')
                return BytesIO(resp.content)

        raise ValueError('source only accept a2f or acr')

    async def get_data_update(self) -> DataUpdate:
        """Get the latest version of Arcaea client."""

        return await self._aua_request_json(Endpoint.Data.update, {}, DataUpdate)

    async def get_data_theory(
            self,
            overflow: Optional[int] = None,
            with_recent: Optional[bool] = None,
            with_song_info: Optional[bool] = None,
            version: Optional[str] = None
    ) -> DataTheory:
        """
        Get the best 30 score under the given version with a theory player.

        :param overflow: (Optional) number, range 0-10. The number of the overflow records below the best30 minimum
        :param with_recent: (Optional) boolean. if true, will reply with recent_score
        :param with_song_info: (Optional) boolean. if true, will reply with songinfo
        :param version: (Optional) string, formatted like '4.0'. The version of Arcaea.
        """

        if overflow and overflow not in range(11):
            raise ValueError('overflow only accept 0-10')

        return await self._aua_request_json(Endpoint.Data.theory, set_params(**locals()), DataTheory)

    async def get_data_challenge(
            self,
            path: str,
            body: Optional[dict] = None,
            time: Optional[int] = None
    ) -> DataChallenge:
        """
        Get the X-Random-Challenge value.

        Note: It is designed for the release version of AUA, and not available for the release version.

        :param path: request arcapi path
        :param body: (Optional) request body
        :param time: (Optional) request timestamp
        """

        if body:
            body = urlencode(body)

        return await self._aua_request_json(Endpoint.Data.challenge, set_params(**locals()), DataChallenge)

    async def get_data_cert(self) -> DataCert:
        """Get the latest cert of Arcaea client"""

        return await self._aua_request_json(Endpoint.Data.cert, {}, DataCert)
