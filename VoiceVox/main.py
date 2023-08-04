from Audio import Audio
from VoiceVox import VoiceVox
import PySimpleGUI as GUI


# メイン関数
if __name__ == '__main__':

    audio = Audio()
    voicevox = VoiceVox(2)

    # GUI設定
    GUI.theme("DarkBlue")
    layout=[
        [GUI.Text("読み上げ文章を入力")],
        [GUI.InputText("", key="text")],
        [GUI.Button("読み上げ", key="ok")]]
    
    # ウィンドウを開く
    window=GUI.Window("VoiceVox Reader", layout, return_keyboard_events=True)

    # イベントループ
    while True:
        event, values=window.read()
        # ウィンドウクローズ
        if event == GUI.WIN_CLOSED:
            break
        # 読み上げボタン押下もしくはESCキー入力
        elif event=="ok" or event == 'Escape:27':
            text=values["text"]            
            audio.output(voicevox.create(text))
