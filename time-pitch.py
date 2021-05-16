import numpy as np
import librosa
from librosa import display
import matplotlib.pyplot as plt

# music file
librosa_ex = librosa.ex('trumpet')
audio_path_1 = './1.mp3'
audio_path_2 = './2.mp3'
audio_path_3 = './3.mp3'

# Default

n_fft = 4096
hop_length = 512

# Visualizing audio and f0 base frequency


def generate_spectrogram(audio, n_fft=4096, hop_length=512):
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

    #plt.show()

    return {"x": f0_times, "y": f0}


# Input: Audio Files -> Return: Each f0 arrays [nx1]
def generate_f0(my_audio, target_audio):

    my_data = generate_spectrogram(my_audio)
    target_data = generate_spectrogram(target_audio)

    return [my_data, target_data]


result = generate_f0(librosa_ex, audio_path_1)

for re in result:
    for r in re:
        print(r)

        # 원본 데이터와 인덱스(길이)가 같게
        # ndarray 사용
