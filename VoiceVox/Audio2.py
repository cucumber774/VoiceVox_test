import pyaudio

# オーディオ関連処理クラス
class Audio(object):

    # コンストラクタ
    def __init__(self):
        # オーディオと出力ストリームのオープン
        self.audio = pyaudio.PyAudio()
  
        self.stream = self.audio.open(
            format=8,
            channels=1,
	        rate=24000,
            output_device_index=2,
            output=True)
    
    # デストラクタ
    def __del__(self):
        # オーディオと出力ストリームのクローズ
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    # 音声出力
    def output(self, inSound):
        self.stream.write(inSound)





