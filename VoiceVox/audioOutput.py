import pyaudio

class audioOutput(object):

    def __init__(self):
        self.audio = pyaudio.PyAudio()
  
        self.stream = self.audio.open(
            format=8,
            channels=1,
	        rate=24000,
            output=True)

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def output(self, sound):
        self.stream.write(sound)





