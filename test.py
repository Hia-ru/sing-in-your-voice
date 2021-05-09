import numpy as np
import librosa, librosa.display 
import matplotlib.pyplot as plt

FIG_SIZE = (15,10)
audio_path = './25-21.mp3'
sig , sr = librosa.load(audio_path)
#print(type(x[0]), type(sr))
# <class 'numpy.ndarray'> <class 'int'>

#print(x, sr)

print(len(sig))
sig = sig[:round(len(sig)/8)]
time = np.linspace(0, len(sig)/sr, len(sig))

# STFT -> spectrogram
hop_length = 512  # 전체 frame 수
n_fft = 2048  # frame 하나당 sample 수

# calculate duration hop length and window in seconds
hop_length_duration = float(hop_length)/sr
n_fft_duration = float(n_fft)/sr

# STFT
stft = librosa.stft(sig, n_fft=n_fft, hop_length=hop_length)
#print(stft[0])
# 복소공간 값 절댓값 취하기
magnitude = np.abs(stft)
#print(type(magnitude))
# magnitude >> Decibels 
log_spectrogram = librosa.amplitude_to_db(magnitude)
print(max(log_spectrogram[0]))


# for i in range(0,100):
#     print(max(log_spectrogram[i]))

# #display spectrogram
# plt.figure(figsize=FIG_SIZE)
# librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.colorbar(format="%+2.0f dB")
# plt.title("Spectrogram (dB)")
# plt.show()
