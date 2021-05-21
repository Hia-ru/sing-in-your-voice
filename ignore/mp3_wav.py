from pydub import AudioSegment
AudioSegment.from_file("3.mp3").export("3.wav", format="wav", bitrate="16k")

import librosa

audio, sr = librosa.load('3.wav', sr=16000)
print('sr:', sr, ', audio shape:', audio.shape)
print('length:', audio.shape[0]/float(sr), 'secs')
