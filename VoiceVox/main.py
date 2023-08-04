
import json
import requests
from audioOutput import audioOutput
import PySimpleGUI

# 文章読み上げ
def readText (text, speaker=2, filepath='./audio.wav'):
    host = 'localhost'
    port = 50021

    # 読み上げ文章と音声指定のクエリ
    params = (
        ('text', text),
        ('speaker', speaker),
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

    a = audioOutput()
    a.output(response_main.content)

if __name__ == '__main__':
    text = 'マイクテストマイクテスト、本日も晴天なり'
    readText(text)