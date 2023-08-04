import json
import requests

host = 'localhost'
port = 50021

# VoiceVox�֘A�����N���X
class VoiceVox(object):


    # �R���X�g���N�^    
    def __init__(self, inSpeaker):
        self.speaker = inSpeaker

    # �ǂݏグ�����쐬
    def create (self, inText):

        # �ǂݏグ���͂Ɖ����w��̃N�G��
        params = (
            ('text', inText),
            ('speaker', self.speaker),
        )
        response_query = requests.post(
            f'http://{host}:{port}/audio_query',
            params=params
        )

        # �ǂݏグ�����쐬
        headers = {'Content-Type': 'application/json',}
        response_main = requests.post(
            f'http://{host}:{port}/synthesis',
            headers=headers,
            params=params,
            data=json.dumps(response_query.json())
        )
        return response_main.content