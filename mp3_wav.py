from pydub import AudioSegment
AudioSegment.from_file("iuiu.mp3").export("iuiu.wav", format="wav", bitrate="16k")

import librosa

audio, sr = librosa.load('iuiu.wav', sr=16000)
print('sr:', sr, ', audio shape:', audio.shape)
print('length:', audio.shape[0]/float(sr), 'secs')