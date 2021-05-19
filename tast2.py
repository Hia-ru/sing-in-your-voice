import numpy as np
import librosa
from librosa import display
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.arrayprint import DatetimeFormat
import soundfile as sf
from edit import edit_L
import copy


audio_path = './2.mp3'
sig , sr = librosa.load(audio_path)
size=sr*5
sig = sig[0:size]
# si = sig[0:sr*3]
# print(len(sig))
# print(len(si))
# si = librosa.effects.time_stretch(si,0.5)
# print(len(si))


#hop_length = 512  # 전체 frame 수
# n_fft = 2048  # frame 하나당 sample 수
# n = len(sig)
# y_pad = librosa.util.fix_length(sig, n + n_fft // 2)
sig2=sig
print(librosa.effects.split(sig2, top_db=30))

# print(sp)

# STFT
stft = librosa.stft(sig, n_fft=512)
magnitude = np.abs(stft)
log_spectrogram = librosa.amplitude_to_db(magnitude)
print(len(librosa.times_like(log_spectrogram)))
# 피치조절 & 박자조절
# i_= int(sr*sec/2)
# t=sig[0:i_]
# nt=sig[i_+1:]
# #sig[0:i_] = librosa.effects.pitch_shift(sig[0:i_],sr,2)
# t = librosa.effects.time_stretch(t,1.2)
# sig = np.r_[t,nt]
#print(stft)
#역변환
# inv_ls = librosa.griffinlim(log_spectrogram)
# inv = librosa.istft(stft, length=n)

#sf.write('stereo_file.wav', sig, sr, 'PCM_24')
sig, voiced_flag, voiced_probs = librosa.pyin(sig,librosa.note_to_hz('C2'),librosa.note_to_hz('C7'))

##plot1
fig, ax = plt.subplots()
img = librosa.display.specshow(log_spectrogram, sr=sr, x_axis='time', y_axis='log', ax=ax)
times = librosa.times_like(sig)
print(len(times))
fig.colorbar(img, ax=ax, format="%+2.f dB")
ax.plot(times, sig, label='f0', color='cyan', linewidth=3)
ax.legend(loc='upper right')
plt.show()

# step = sec/(len(pit)-1)
# lis = [0 for i in range(len(pit))]

# for i in range(len(lis)):
#     lis[i] = i*step



# for i in range(len(pit)):
#     pit2[i] = np.array([pit[i],lis[i]])
#     print([pit2[i]])


#pit = np.array([pit,lis])
# plt.plot(lis, pit)
# plt.yscale("log")
# plt.show()
# print(pit.shape)
##plot2
# times = librosa.times_like(pit)
# fig, ax = plt.subplots()
# img = librosa.display.specshow(pit, x_axis='time', y_axis='log', ax=ax)
# ax.set(title='pYIN fundamental frequency estimation')
# fig.colorbar(img, ax=ax, format="%+2.f dB")
# ax.plot(times, pit, label='f0', color='cyan', linewidth=3)
# ax.legend(loc='upper right')

