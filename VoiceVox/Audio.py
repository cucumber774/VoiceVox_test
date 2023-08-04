import pyaudio

# オーディオ関連処理クラス
class Audio(object):

    # コンストラクタ
    def __init__(self):
        # オーディオと出力ストリームのオープン
        self.audio = pyaudio.PyAudio()

        # 仮想オーディオのインデックスを探す
        for deviceIndex in range(self.audio.get_device_count()):
            data = self.audio.get_device_info_by_index(deviceIndex)
            if data.get('name') == 'CABLE Input (VB-Audio Virtual C':
                break

        # 仮想オーディオが無かった
        if deviceIndex is self.audio.get_device_count():
            assert()

        # ストリームを開く
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
	        channels=1,
            rate=24000,
            output=True,
            output_device_index=deviceIndex)
    
    # デストラクタ
    def __del__(self):
        # オーディオと出力ストリームのクローズ
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    # 音声出力
    def output(self, inSound):
        self.stream.write(inSound)





