import tempfile
import time
from gtts import gTTS
from pygame import mixer


def save_n_speak(word):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=word, lang='zh-tw')
        # tts = gTTS('bonjour', lang='zh-tw')

        tts.save('{}.mp3'.format(fp.name))
        print("saved")
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
        time.sleep(3)
        print("played")


def save(word):
    tts = gTTS(text=word, lang='zh-tw')
    tts.save('i_am_good.mp3')
    print("saved")
    return ('i_am_good.mp3')


def speak(mp3):
    mixer.init()
    mixer.music.load(mp3)
    print('loaded')
    mixer.music.play()
    time.sleep(1)
    print("played")


if __name__ == "__main__":
    save_n_speak('你真係on9')
#     speak(save('i am good'))
