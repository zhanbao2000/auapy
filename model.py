from typing import Optional, Union

from pydantic import BaseModel


class AccountInfo(BaseModel):
    code: str
    name: str
    user_id: int
    is_mutual: bool
    is_char_uncapped_override: bool
    is_char_uncapped: bool
    is_skill_sealed: bool
    rating: int
    join_date: int
    character: int


class Record(BaseModel):
    user_id: Optional[int]
    score: int
    health: int
    rating: float
    song_id: str
    modifier: int
    difficulty: int
    clear_type: int
    best_clear_type: int
    time_played: int  # milliseconds
    near_count: int
    miss_count: int
    perfect_count: int
    shiny_perfect_count: int


class Chart(BaseModel):
    name_en: str
    name_jp: str
    artist: str
    bpm: str
    bpm_base: float
    set: str
    set_friendly: str
    time: int
    side: int
    world_unlock: bool
    remote_download: bool
    bg: str
    date: int
    version: str
    difficulty: int
    rating: int
    note: int
    chart_designer: str
    jacket_designer: str
    jacket_override: bool
    audio_override: bool


class Song(BaseModel):
    song_id: str
    difficulties: list[Chart]
    alias: list[str]


class BaseResponse(BaseModel):
    class Content(BaseModel):
        ...

    status: int
    content: Optional[Content]
    message: Optional[str]


class UserInfo(BaseResponse):
    class Content(BaseModel):
        account_info: AccountInfo
        recent_score: Optional[list[Record]]
        songinfo: Optional[list[Chart]]

    content: Optional[Content]


class UserBest(BaseResponse):
    class Content(BaseModel):
        account_info: AccountInfo
        record: Record
        songinfo: Optional[list[Chart]]
        recent_score: Optional[Record]
        recent_songinfo: Optional[Chart]

    content: Optional[Content]


class UserBest30(BaseResponse):
    class Content(BaseModel):
        best30_avg: float
        recent10_avg: float
        account_info: AccountInfo
        best30_list: list[Record]
        best30_songinfo: Optional[list[Chart]]
        recent_score: Optional[Record]
        recent_songinfo: Optional[Chart]

    content: Optional[Content]


class SongInfo(BaseResponse):
    class Content(BaseModel):
        song_id: str
        difficulties: list[Chart]
        alias: list[str]

    content: Optional[Content]


class SongList(BaseResponse):
    class Content(BaseModel):
        songs: list[Song]

    class TooManyRecords(BaseModel):
        songs: list[str]

    content: Union[Content, TooManyRecords]


class SongAlias(BaseResponse):
    content: Optional[list[str]]


class SongRandom(BaseResponse):
    class Content(BaseModel):
        id: str
        ratingClass: int
        songinfo: Optional[Chart]

    content: Optional[Content]


class DataUpdate(BaseResponse):
    class Content(BaseModel):
        url: str
        version: str

    content: Optional[Content]


class DataTheory(BaseResponse):
    class Content(BaseModel):
        best30_avg: float
        recent10_avg: float
        account_info: AccountInfo
        best30_list: list[Record]
        best30_songinfo: Optional[list[Chart]]
        recent_score: Optional[Record]
        recent_songinfo: Optional[Chart]

    content: Optional[Content]


class DataChallenge(BaseResponse):
    content: Optional[str]


class DataCert(BaseResponse):
    class Content(BaseModel):
        entry: str
        version: str
        cert: str
        password: str

    content: Optional[Content]
