import time
import board
import digitalio
import random

from audiomp3 import MP3Decoder

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

button1 = digitalio.DigitalInOut(board.GP20)
button1.switch_to_input(pull=digitalio.Pull.UP)

# Replace with your mp3files name
mp3files = ["start-the-day-with-3lber.mp3", "10lber-bro.mp3",
            "did-that-just-happen.mp3", "game-changer.mp3",
            "lets-go.mp3", "never-give-up.mp3", "3lber-scream.mp3",
            "pinecone.mp3", "omg-6lber.mp3", "game-over.mp3",
            "long-as-leg.mp3"]



# You have to specify some mp3 file when creating the decoder
mp3 = open(mp3files[0], "rb")
decoder = MP3Decoder(mp3)
audio = AudioOut(board.GP18)

while True:
    if not button1.value:
        file = random.randint(0,10)
        try:
            decoder.file = open(mp3files[file], "rb")
            audio.play(decoder)
            print("playing", mp3files[file])
        except:
            print("error playing mp3 file: %s" %file)


        t = time.monotonic()
        s = 0
        
        if file == 0:
            s = 6
        elif file == 1:
            s = 3
        elif file == 2:
            s = 3
        elif file == 3:
            s = 5
        elif file == 4:
            s = 8
        elif file == 5:
            s = 10
        elif file == 6:
            s = 8
        elif file == 7:
            s = 5
        elif file == 8:
            s = 2
        elif file == 9:
            s = 7
        elif file == 10:
            s = 2

# 3lber-scream 8 sec
# 10ber-bro 3 sec
# did-that-just-happen 3 sec
# game-changer 5 sec
# lets-go 8 sec
# never-give-up 10 sec
# start-the-day-with-3lber 6 sec
# pinecone 5 sec
# omg-6lber 2 sec
# game-over 7 sec
# long-as-leg 2 sec

        while time.monotonic() - t < s:
            pass