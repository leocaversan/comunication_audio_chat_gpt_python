
import sounddevice as sd
from scipy.io.wavfile import write

def recorder(sec = 5):
    fs = 44100
    seconds = sec
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write('content/output.wav', fs, myrecording)  

    return 'content/output.wav'