import sounddevice
import wavio
from scipy.io.wavfile import write
frequency  = 44100
duration = 5
print("recoding...")
recordAudio = sounddevice.rec(int(duration*frequency),samplerate=frequency,channels=2)
sounddevice.wait()
write(r"C:\Users\vijay\OneDrive\Desktop\short projects\audio recorder\recording.wav",frequency,recordAudio)
