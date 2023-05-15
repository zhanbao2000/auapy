class ArcaeaUnlimitedAPIEndpoint:
    class User:
        info: str = '/user/info'
        best: str = '/user/best'
        bests_session: str = '/user/bests/session'
        bests_result: str = '/user/bests/result'

    class Song:
        info: str = '/song/info'
        list: str = '/song/list'
        alias: str = '/song/alias'
        random: str = '/song/random'

    class Assets:
        icon: str = '/assets/icon'
        char: str = '/assets/char'
        song: str = '/assets/song'
        aff: str = '/assets/aff'
        preview: str = '/assets/preview'

    class Data:
        update: str = '/data/update'
        theory: str = '/data/theory'
        challenge: str = '/data/challenge'
        cert: str = '/data/cert'
