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
    time_played: int
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


class UserInfo(BaseModel):
    class Content(BaseModel):
        account_info: AccountInfo
        recent_score: list[Record]
        songinfo: list[Chart]

    status: int
    content: Optional[Content]
    message: Optional[str]


class UserBest(BaseModel):
    class Content(BaseModel):
        account_info: AccountInfo
        record: Record
        songinfo: list[Chart]
        recent_score: Record
        recent_songinfo: Chart

    status: int
    content: Optional[Content]
    message: Optional[str]


class UserBest30(BaseModel):
    class Content(BaseModel):
        best30_avg: float
        recent10_avg: float
        account_info: AccountInfo
        best30_list: list[Record]
        best30_songinfo: list[Chart]
        recent_score: Record
        recent_songinfo: Chart

    status: int
    content: Optional[Content]
    message: Optional[str]


class SongInfo(BaseModel):
    class Content(BaseModel):
        song_id: str
        difficulties: list[Chart]
        alias: list[str]

    status: int
    content: Optional[Content]
    message: Optional[str]


class SongList(BaseModel):
    class Content(BaseModel):
        songs: list[Song]

    class TooManyRecords(BaseModel):
        songs: list[str]

    status: int
    content: Union[Content, TooManyRecords]
    message: Optional[str]


class SongAlias(BaseModel):
    status: int
    content: Optional[list[str]]
    message: Optional[str]


class SongRandom(BaseModel):
    class Content(BaseModel):
        id: str
        ratingClass: int
        songinfo: Chart

    status: int
    content: Optional[Content]
    message: Optional[str]


class DataUpdate(BaseModel):
    class Content(BaseModel):
        url: str
        version: str

    status: int
    content: Optional[Content]
    message: Optional[str]


class DataTheory(BaseModel):
    class Content(BaseModel):
        best30_avg: float
        recent10_avg: float
        account_info: AccountInfo
        best30_list: list[Record]
        best30_songinfo: list[Chart]
        recent_score: Record
        recent_songinfo: Chart

    status: int
    content: Optional[Content]
    message: Optional[str]


class DataChallenge(BaseModel):
    status: int
    content: Optional[str]
    message: Optional[str]


class DataCert(BaseModel):
    class Content(BaseModel):
        entry: str
        version: str
        cert: str
        password: str

    status: int
    content: Optional[Content]
    message: Optional[str]
