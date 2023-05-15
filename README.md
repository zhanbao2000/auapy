# <p align="center">auapy
<p align="center">Call ArcaeaUnlimitedAPI in your python projects.

## Requirements

 - httpx~=0.23.3
 - pydantic~=1.10.4
 - pytest~=7.2.1
 - pytest-asyncio~=0.16.0

```bash
pip install -r requirements.txt
```

## Usage

```python
from auapy import ArcaeaUnlimitedAPIClient

async def main():
    
    client = ArcaeaUnlimitedAPIClient(
        'http://localhost:61658/botarcapi',
        'Yout User Agent',
        'Your Bearer Token'
    )

    user_info = await client.get_user_info('ToasterKoishi', recent=5, withsonginfo=True)
    print(user_info.content.account_info.rating)

    song_info = await client.get_song_info(song_id='infinityheaven')
    print(song_info.content.difficulties[0].name_en)
```


## Supported endpoints

- [x] [user/info](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/user/info.md)
- [x] [user/best](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/user/best.md)
- [x] [user/bests/session](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/user/bests/session.md) (without unit test)
- [x] [user/bests/result](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/user/bests/result.md) (without unit test)
- [x] [song/info](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/song/info.md)
- [x] [song/list](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/song/list.md)
- [x] [song/alias](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/song/alias.md)
- [x] [song/random](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/song/random.md)
- [x] [assets/icon](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/assets/icon.md)
- [x] [assets/char](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/assets/char.md)
- [x] [assets/song](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/assets/song.md)
- [x] [assets/preview](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/assets/preview.md)
- [x] [data/update](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/data/update.md)
- [x] [data/theory](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/data/theory.md)
- [x] [data/challenge](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/data/challenge.md)
- [x] [data/cert](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/data/cert.md)
- [ ] [image/user/*](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs/blob/main/image/user.md)

## Credits

 - [UnofficialArcaeaAPI.Docs](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Docs)
 - [UnofficialArcaeaAPI.Lib](https://github.com/Arcaea-Infinity/UnofficialArcaeaAPI.Lib)
 - [ArcaeaUnlimitedAPI-Wiki](https://github.com/Arcaea-Infinity/ArcaeaUnlimitedAPI-Wiki)
 - [ArcaeaUnlimitedAPI.Lib](https://github.com/Arcaea-Infinity/ArcaeaUnlimitedAPI.Lib)
 - [ArcaeaChartRender](https://github.com/Arcaea-Infinity/ArcaeaChartRender)
 - [Aff2Preview](https://github.com/Arcaea-Infinity/Aff2Preview)
