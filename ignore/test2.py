import numpy as np
import librosa
from librosa import display
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.arrayprint import DatetimeFormat
from numpy.core.numeric import True_
import soundfile as sf
from edit import edit_L
import copy
from edit import generate_f0

audio_path = './2.mp3'
sig , sr = librosa.load(audio_path)
size=sr*5
sig = sig[0:size]

audio_path = './test.mp3'
yy , sr = librosa.load(audio_path)

generate_f0(sig,sr,show_graph=True)
generate_f0(yy,sr,show_graph=True)

# STFT
# stft = librosa.stft(sig, n_fft=512)
# magnitude = np.abs(stft)
# log_spectrogram = librosa.amplitude_to_db(magnitude)
# print(len(librosa.times_like(log_spectrogram)))
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
#sig, voiced_flag, voiced_probs = librosa.pyin(sig,librosa.note_to_hz('C2'),librosa.note_to_hz('C7'))

##plot1
# fig, ax = plt.subplots()
# img = librosa.display.specshow(log_spectrogram, sr=sr, x_axis='time', y_axis='log', ax=ax)
# times = librosa.times_like(sig)
# fig.colorbar(img, ax=ax, format="%+2.f dB")
# ax.plot(times, sig, label='f0', color='cyan', linewidth=3)
# ax.legend(loc='upper right')
# plt.show()


