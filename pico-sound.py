import time
import board
import digitalio

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
mp3files = ["start-the-day-with-3lber.mp3"]

# You have to specify some mp3 file when creating the decoder
mp3 = open(mp3files[0], "rb")
decoder = MP3Decoder(mp3)
audio = AudioOut(board.GP18)

while True:
    if not button1.value:
        decoder.file = open(mp3files[0], "rb")
        audio.play(decoder)
        print("playing", mp3files[0])

        t = time.monotonic()
        while time.monotonic() - t < 6:
            pass