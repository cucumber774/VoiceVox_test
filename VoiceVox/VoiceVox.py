import json
import requests

host = 'localhost'
port = 50021

# VoiceVox関連処理クラス
class VoiceVox(object):


    # コンストラクタ    
    def __init__(self, inSpeaker):
        self.speaker = inSpeaker

    # 読み上げ音声作成
    def create (self, inText):

        # 読み上げ文章と音声指定のクエリ
        params = (
            ('text', inText),
            ('speaker', self.speaker),
        )
        response_query = requests.post(
            f'http://{host}:{port}/audio_query',
            params=params
        )

        # 読み上げ音声作成
        headers = {'Content-Type': 'application/json',}
        response_main = requests.post(
            f'http://{host}:{port}/synthesis',
            headers=headers,
            params=params,
            data=json.dumps(response_query.json())
        )
        return response_main.content