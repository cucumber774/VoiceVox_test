from Audio import Audio
from VoiceVox import VoiceVox
import PySimpleGUI as GUI


# メイン関数
if __name__ == '__main__':

    audio = Audio()
    voicevox = VoiceVox(2)

    GUI.theme("DarkBlue")
    layout=[
        [GUI.Text("読み上げ文章を入力")],
        [GUI.InputText("テキストを入力", key="text")],
        [GUI.Button("読み上げ", key="ok")]]
    
    window=GUI.Window("VoiceVox Reader", layout)

    while True:
        event, values=window.read()
        if event == GUI.WIN_CLOSED:
            break
        elif event=="ok":
            text=values["text"]            
            audio.output(voicevox.create(text))
