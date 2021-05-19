import librosa
from librosa import display
import numpy as np
import matplotlib.pyplot as plt

audio_path = './2.mp3'
y, sr = librosa.load(audio_path)
size=sr*5
y = y[0:size]
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
times = librosa.times_like(f0)
for f in f0:
    if np.isnan(f):
        f = 1
print(librosa.effects.split(f0, top_db=30))

D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
fig, ax = plt.subplots()
img = display.specshow(D, x_axis='time', y_axis='log', ax=ax)
ax.set(title='pYIN fundamental frequency estimation')
#fig.colorbar(img, ax=ax, format="%+2.f dB")
#ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
ax.legend(loc='upper right')
plt.show()

#print(f0)