import numpy as np
import librosa
from librosa import display
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.signal

# music file
librosa_ex = librosa.ex('trumpet')
audio_path_1 = './1.mp3'
audio_path_2 = './2.mp3'
audio_path_3 = './3.mp3'

n_fft = 4096
hop_length = 512

# Visualizing audio and f0 base frequency


def generate_spectrogram(audio, n_fft, hop_length):
    fig, ax = plt.subplots()
    amplitude, sr = librosa.load(audio)
    stft_absolute_values = np.abs(librosa.stft(amplitude))
    db_base_stft = librosa.amplitude_to_db(stft_absolute_values, ref=np.max)
    img = display.specshow(db_base_stft, y_axis='log', x_axis='time', ax=ax)
    ax.set_title('STFT spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")

    # print(db_base_stft)

    # add f0 plot
    f0, voiced_flag_t, voiced_probs_t = librosa.pyin(amplitude, fmin=librosa.note_to_hz('C2'),
                                                     fmax=librosa.note_to_hz('C7'), sr=sr,
                                                     hop_length=hop_length, frame_length=n_fft,
                                                     pad_mode='constant', center=True)
    f0_times = librosa.times_like(f0)

    ax.plot(f0_times, f0, label='f0', color='cyan', linewidth=2)

    # plt.show()


generate_spectrogram(audio_path_1, n_fft, hop_length)
