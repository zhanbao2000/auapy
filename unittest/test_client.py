import pytest

from ..client import ArcaeaUnlimitedAPIClient

client = ArcaeaUnlimitedAPIClient(
    'http://localhost:61658/botarcapi',
    'User Agent',
    'Bearer Token'
)


@pytest.mark.asyncio
async def test_get_user_info():
    assert await client.get_user_info('ToasterKoishi', recent=1, withsonginfo=True)
    assert await client.get_user_info('ToasterKoishi', recent=0, withsonginfo=False)


@pytest.mark.asyncio
async def test_get_user_best():
    assert await client.get_user_best(difficulty=2, user='ToasterKoishi', songid='ifi', withrecent=True, withsonginfo=True)


@pytest.mark.asyncio
async def test_get_user_best30():
    assert await client.get_user_best30('ToasterKoishi', overflow=5, withrecent=True, withsonginfo=True)


@pytest.mark.asyncio
async def test_get_song_info():
    assert await client.get_song_info('infinity')


@pytest.mark.asyncio
async def test_get_song_list():
    assert await client.get_song_list()


@pytest.mark.asyncio
async def test_get_song_random():
    assert await client.get_song_random(start=18, end=21, withsonginfo=True)


@pytest.mark.asyncio
async def test_get_assets_icon():
    assert await client.get_assets_icon(1)


@pytest.mark.asyncio
async def test_get_assets_char():
    assert await client.get_assets_char(1, awakened=True)


@pytest.mark.asyncio
async def test_get_assets_song():
    assert await client.get_assets_song('testify', difficulty=3)


@pytest.mark.asyncio
async def test_get_assets_preview():
    assert await client.get_assets_preview(songid='testify', difficulty=3, source='a2f')
    assert await client.get_assets_preview(songid='testify', difficulty=3, source='acr')


@pytest.mark.asyncio
async def test_get_data_update():
    assert await client.get_data_update()


@pytest.mark.asyncio
async def test_get_data_theory():
    assert await client.get_data_theory(overflow=5, withrecent=True, withsonginfo=True)


@pytest.mark.asyncio
async def test_get_data_challenge():
    assert await client.get_data_challenge('friend/me/delete', {'friend_id': '000114514'})


@pytest.mark.asyncio
async def test_get_data_cert():
    assert await client.get_data_cert()
