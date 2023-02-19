from ..model import *


def test_user_info():

    test_response = {'status': 0, 'content': {'account_info': {'code': '062596721', 'name': 'ToasterKoishi', 'user_id': 4, 'is_mutual': False, 'is_char_uncapped_override': False, 'is_char_uncapped': True, 'is_skill_sealed': False, 'rating': 1274, 'join_date': 1487816563340, 'character': 12}, 'recent_score': [{'score': 9992128, 'health': 100, 'rating': 11.76064, 'song_id': 'macromod', 'modifier': 2, 'difficulty': 2, 'clear_type': 2, 'best_clear_type': 2, 'time_played': 1651198101733, 'near_count': 2, 'miss_count': 0, 'perfect_count': 1115, 'shiny_perfect_count': 1081}, {'score': 9982099, 'health': 100, 'rating': 11.510494999999999, 'song_id': 'espebranch', 'modifier': 0, 'difficulty': 2, 'clear_type': 2, 'best_clear_type': 3, 'time_played': 1651045525836, 'near_count': 4, 'miss_count': 0, 'perfect_count': 1054, 'shiny_perfect_count': 1003}], 'songinfo': [{'name_en': 'MacrocosmicModulation', 'name_jp': '', 'artist': 'JAKAZiD', 'bpm': '170', 'bpm_base': 170.0, 'set': 'single', 'set_friendly': 'MemoryArchive', 'time': 147, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'single2_light', 'date': 1645056004, 'version': '3.12', 'difficulty': 19, 'rating': 98, 'note': 1117, 'chart_designer': 'Exschwas↕on', 'jacket_designer': '装甲枕', 'jacket_override': False, 'audio_override': False}, {'name_en': 'LunarOrbit-believeintheEspebranchroad-', 'name_jp': '白道、多希望羊と信じありく。', 'artist': 'Apo11oprogramft.大瀬良あい', 'bpm': '192', 'bpm_base': 192.0, 'set': 'base', 'set_friendly': 'Arcaea', 'time': 141, 'side': 1, 'world_unlock': True, 'remote_download': False, 'bg': 'mirai_conflict', 'date': 1535673600, 'version': '1.7', 'difficulty': 18, 'rating': 96, 'note': 1058, 'chart_designer': '月刊Toaster', 'jacket_designer': 'hideo', 'jacket_override': False, 'audio_override': False}]}}
    assert UserInfo(**test_response).content.account_info.code == '062596721'


def test_user_best():

    test_response = {'status': 0, 'content': {'account_info': {'code': '062596721', 'name': 'ToasterKoishi', 'user_id': 4, 'is_mutual': False, 'is_char_uncapped_override': False, 'is_char_uncapped': True, 'is_skill_sealed': False, 'rating': 1282, 'join_date': 1487816563340, 'character': 12}, 'record': {'score': 9979257, 'health': 100, 'rating': 12.796285000000001, 'song_id': 'ifi', 'modifier': 0, 'difficulty': 2, 'clear_type': 1, 'best_clear_type': 5, 'time_played': 1598919831344, 'near_count': 5, 'miss_count': 1, 'perfect_count': 1570, 'shiny_perfect_count': 1466}, 'songinfo': [{'name_en': '#1f1e33', 'name_jp': '', 'artist': 'かめりあ(EDP)', 'bpm': '181', 'bpm_base': 181.0, 'set': 'vs', 'set_friendly': 'Black Fate', 'time': 163, 'side': 1, 'world_unlock': False, 'remote_download': True, 'bg': 'vs_conflict', 'date': 1590537604, 'version': '3.0', 'difficulty': 21, 'rating': 109, 'note': 1576, 'chart_designer': '夜浪 VS 東星 "Convergence"', 'jacket_designer': '望月けい', 'jacket_override': False, 'audio_override': False}], 'recent_score': {'user_id': 4, 'score': 9963377, 'health': 100, 'rating': 12.316885, 'song_id': 'lightningscrew', 'modifier': 0, 'difficulty': 2, 'clear_type': 1, 'best_clear_type': 3, 'time_played': 1676588872873, 'near_count': 1, 'miss_count': 4, 'perfect_count': 1187, 'shiny_perfect_count': 1129}, 'recent_songinfo': {'name_en': 'Lightning Screw', 'name_jp': '', 'artist': 'HiTECH NINJA', 'bpm': '190', 'bpm_base': 190.0, 'set': 'dividedheart', 'set_friendly': 'Divided Heart', 'time': 127, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'hime_light', 'date': 1639008004, 'version': '3.10', 'difficulty': 20, 'rating': 105, 'note': 1192, 'chart_designer': '東星', 'jacket_designer': 'シエラ', 'jacket_override': False, 'audio_override': False}}}
    assert UserBest(**test_response).content.record.score == 9979257


def test_user_best30():

    test_response = {'status': 0, 'content': {'best30_avg': 12.707672500000001, 'recent10_avg': 12.836982499999998, 'account_info': {'code': '062596721', 'name': 'ToasterKoishi', 'user_id': 4, 'is_mutual': False, 'is_char_uncapped_override': False, 'is_char_uncapped': True, 'is_skill_sealed': False, 'rating': 1274, 'join_date': 1487816563340, 'character': 12}, 'best30_list': [{'score': 9956548, 'health': 100, 'rating': 13.082740000000001, 'song_id': 'grievouslady', 'modifier': 0, 'difficulty': 2, 'clear_type': 1, 'best_clear_type': 5, 'time_played': 1614911430950, 'near_count': 7, 'miss_count': 3, 'perfect_count': 1440, 'shiny_perfect_count': 1376}], 'best30_songinfo': [{'name_en': 'Grievous Lady', 'name_jp': '', 'artist': 'Team Grimoire vs Laur', 'bpm': '210', 'bpm_base': 210.0, 'set': 'yugamu', 'set_friendly': 'Vicious Labyrinth', 'time': 141, 'side': 1, 'world_unlock': False, 'remote_download': True, 'bg': 'grievouslady', 'date': 1509667208, 'version': '1.5', 'difficulty': 22, 'rating': 113, 'note': 1450, 'chart_designer': '迷路深層', 'jacket_designer': 'シエラ', 'jacket_override': False, 'audio_override': False}], 'recent_score': {'user_id': 4, 'score': 9982099, 'health': 100, 'rating': 11.510494999999999, 'song_id': 'espebranch', 'modifier': 0, 'difficulty': 2, 'clear_type': 2, 'best_clear_type': 3, 'time_played': 1651045525836, 'near_count': 4, 'miss_count': 0, 'perfect_count': 1054, 'shiny_perfect_count': 1003}, 'recent_songinfo': {'name_en': 'LunarOrbit -believe in the Espebranch road-', 'name_jp': '白道、多希望羊と信じありく。', 'artist': 'Apo11o program ft. 大瀬良あい', 'bpm': '192', 'bpm_base': 192.0, 'set': 'base', 'set_friendly': 'Arcaea', 'time': 141, 'side': 1, 'world_unlock': True, 'remote_download': False, 'bg': 'mirai_conflict', 'date': 1535673600, 'version': '1.7', 'difficulty': 18, 'rating': 96, 'note': 1058, 'chart_designer': '月刊Toaster', 'jacket_designer': 'hideo', 'jacket_override': False, 'audio_override': False}}}
    assert UserBest30(**test_response).content.best30_list[0].score == 9956548


def test_song_info():

    test_response = {'status': 0, 'content': {'song_id': 'infinityheaven', 'difficulties': [{'name_en': 'Infinity Heaven', 'name_jp': '', 'artist': 'HyuN', 'bpm': '160', 'bpm_base': 160.0, 'set': 'base', 'set_friendly': 'Arcaea', 'time': 154, 'side': 0, 'world_unlock': False, 'remote_download': False, 'bg': '', 'date': 1491868800, 'version': '1.0', 'difficulty': 2, 'rating': 15, 'note': 336, 'chart_designer': 'Nitro', 'jacket_designer': 'Tagtraume', 'jacket_override': False, 'audio_override': False}, {'name_en': 'Infinity Heaven', 'name_jp': '', 'artist': 'HyuN', 'bpm': '160', 'bpm_base': 160.0, 'set': 'base', 'set_friendly': 'Arcaea', 'time': 154, 'side': 0, 'world_unlock': False, 'remote_download': False, 'bg': '', 'date': 1491868800, 'version': '1.0', 'difficulty': 10, 'rating': 55, 'note': 545, 'chart_designer': 'Nitro', 'jacket_designer': 'Tagtraume', 'jacket_override': False, 'audio_override': False}, {'name_en': 'Infinity Heaven', 'name_jp': '', 'artist': 'HyuN', 'bpm': '160', 'bpm_base': 160.0, 'set': 'base', 'set_friendly': 'Arcaea', 'time': 154, 'side': 0, 'world_unlock': False, 'remote_download': False, 'bg': '', 'date': 1491868800, 'version': '1.0', 'difficulty': 14, 'rating': 75, 'note': 853, 'chart_designer': 'Nitro', 'jacket_designer': 'Tagtraume', 'jacket_override': False, 'audio_override': False}, {'name_en': 'Infinity Heaven', 'name_jp': '', 'artist': 'HyuN', 'bpm': '160', 'bpm_base': 160.0, 'set': 'base', 'set_friendly': 'Arcaea', 'time': 154, 'side': 0, 'world_unlock': False, 'remote_download': False, 'bg': '', 'date': 1590537602, 'version': '3.0', 'difficulty': 18, 'rating': 96, 'note': 986, 'chart_designer': 'Nitr∞', 'jacket_designer': 'Tagtraume', 'jacket_override': True, 'audio_override': False}], 'alias': ['无限天堂', '无尽天堂']}}
    assert SongInfo(**test_response).content.difficulties[0].name_en == 'Infinity Heaven'


def test_song_list():

    test_response = {'status': 0, 'content': {'songs': [{'song_id': 'filament', 'difficulties': [{'name_en': 'Filament', 'name_jp': '', 'artist': 'Puru', 'bpm': '170', 'bpm_base': 170.0, 'set': 'single', 'set_friendly': 'Memory Archive', 'time': 143, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'omatsuri_light', 'date': 1574726400, 'version': '2.4', 'difficulty': 8, 'rating': 45, 'note': 582, 'chart_designer': 'Toaster', 'jacket_designer': 'Hanamori Hiro', 'jacket_override': False, 'audio_override': False}, {'name_en': 'Filament', 'name_jp': '', 'artist': 'Puru', 'bpm': '170', 'bpm_base': 170.0, 'set': 'single', 'set_friendly': 'Memory Archive', 'time': 143, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'omatsuri_light', 'date': 1574726400, 'version': '2.4', 'difficulty': 14, 'rating': 75, 'note': 780, 'chart_designer': 'Toaster', 'jacket_designer': 'Hanamori Hiro', 'jacket_override': False, 'audio_override': False}, {'name_en': 'Filament', 'name_jp': '', 'artist': 'Puru', 'bpm': '170', 'bpm_base': 170.0, 'set': 'single', 'set_friendly': 'Memory Archive', 'time': 143, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'omatsuri_light', 'date': 1574726400, 'version': '2.4', 'difficulty': 19, 'rating': 97, 'note': 991, 'chart_designer': 'Toaster', 'jacket_designer': 'Hanamori Hiro', 'jacket_override': False, 'audio_override': False}], 'alias': ['灯丝', '灯芯']}]}}
    assert SongList(**test_response).content.songs[0].song_id == 'filament'


def test_song_alias():

    test_response = {'status': 0, 'content': ['色号', '对立色']}
    assert SongAlias(**test_response).content[0] == '色号'


def test_song_random():

    test_response = {'status': 0, 'content': {'id': 'divinelight', 'ratingClass': 2, 'songinfo': {'name_en': 'Divine Light of Myriad', 'name_jp': '光速神授説 - Divine Light of Myriad -', 'artist': 'yoho', 'bpm': '172', 'bpm_base': 172.0, 'set': 'observer_append_2', 'set_friendly': 'Esoteric Order', 'time': 142, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'observer_light', 'date': 1626825602, 'version': '3.7', 'difficulty': 21, 'rating': 108, 'note': 1021, 'chart_designer': '東星※神授', 'jacket_designer': '緋原ヨウ', 'jacket_override': False, 'audio_override': False}}}
    assert SongRandom(**test_response).content.songinfo.name_en == 'Divine Light of Myriad'


def test_data_update():

    test_response = {'status': 0, 'content': {'url': 'https://static-bin.lowiro.com/serve/arcaea_3.11.0c.apk?token=HthO8sS2Fm8sgZvT08zcW4Qjzd0nZAWTgX6LCFDp957ILarc4qqzXUuWMGDMEufV3', 'version': '3.11.0c'}}
    assert DataUpdate(**test_response).content.version == '3.11.0c'


def test_data_theory():

    test_response = {'status': 0, 'content': {'best30_avg': 12.480000000000002, 'recent10_avg': 12.870000000000001, 'account_info': {'code': '000000000', 'name': 'Max Grades - v3.0', 'user_id': 0, 'is_mutual': False, 'is_char_uncapped_override': True, 'is_char_uncapped': True, 'is_skill_sealed': False, 'rating': 1257, 'join_date': 1487980800, 'character': 5}, 'best30_list': [{'score': 10001279, 'health': 100, 'rating': 13.3, 'song_id': 'fractureray', 'modifier': 0, 'difficulty': 2, 'clear_type': 3, 'best_clear_type': 3, 'time_played': 1531699208, 'near_count': 0, 'miss_count': 0, 'perfect_count': 1279, 'shiny_perfect_count': 1279}], 'best30_songinfo': [{'name_en': 'Fracture Ray', 'name_jp': '', 'artist': 'Sakuzyo', 'bpm': '200', 'bpm_base': 200.0, 'set': 'rei', 'set_friendly': 'Luminous Sky', 'time': 154, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'fractureray', 'date': 1531699208, 'version': '1.7', 'difficulty': 22, 'rating': 113, 'note': 1279, 'chart_designer': 'Paradox Zero', 'jacket_designer': 'シエラ', 'jacket_override': False, 'audio_override': False}], 'recent_score': {'score': 10001279, 'health': 100, 'rating': 13.3, 'song_id': 'fractureray', 'modifier': 0, 'difficulty': 2, 'clear_type': 3, 'best_clear_type': 3, 'time_played': 1531699208, 'near_count': 0, 'miss_count': 0, 'perfect_count': 1279, 'shiny_perfect_count': 1279}, 'recent_songinfo': {'name_en': 'Fracture Ray', 'name_jp': '', 'artist': 'Sakuzyo', 'bpm': '200', 'bpm_base': 200.0, 'set': 'rei', 'set_friendly': 'Luminous Sky', 'time': 154, 'side': 0, 'world_unlock': False, 'remote_download': True, 'bg': 'fractureray', 'date': 1531699208, 'version': '1.7', 'difficulty': 22, 'rating': 113, 'note': 1279, 'chart_designer': 'Paradox Zero', 'jacket_designer': 'シエラ', 'jacket_override': False, 'audio_override': False}}}
    assert DataTheory(**test_response).content.best30_avg == 12.480000000000002


def test_data_challenge():

    test_response = {'status': 0, 'content': 'JfdDAIQBAAAkdLOHw7PyRfWyhkJvH1Xzfevm7quQMwOk5Lc99fD1vgesJ8uf5ZJgPfgtYlYGDu1FLk31AaNAYfGocKoRMMSAlqDc4y/aZxXCn4cGjnJ7ovR9rkCQG8W1sJ9cHuK4CDo='}
    assert DataChallenge(**test_response).content == 'JfdDAIQBAAAkdLOHw7PyRfWyhkJvH1Xzfevm7quQMwOk5Lc99fD1vgesJ8uf5ZJgPfgtYlYGDu1FLk31AaNAYfGocKoRMMSAlqDc4y/aZxXCn4cGjnJ7ovR9rkCQG8W1sJ9cHuK4CDo='


def test_data_cert():

    test_response = {'status': 0, 'content': {'entry': 'join/21', 'version': '4.1.4c', 'cert': 'HERE IS THE CERT', 'password': 'HelloWorld'}}
    assert DataCert(**test_response).content.cert == 'HERE IS THE CERT'


def test_on_error():

    test_response = {'status': -8, 'message': 'too many records', 'content': {'songs': ['lostcivilization', 'lastcelebration']}}
    assert SongList(**test_response).content.songs[0] == 'lostcivilization'

    test_response = {'status': -5, 'message': 'invalid songname or songid'}
    assert SongAlias(**test_response).message == 'invalid songname or songid'
