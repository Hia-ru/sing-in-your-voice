import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import soundfile as sf
import librosa as lr
from pydub import AudioSegment
import os

# Read sound data
def read_audio(fileName, sr=22050, n_fft=2048, win_length=2048, hop_length=512, flag_to_draw=False):
    """
    Parameters
    filePath : Path of Sound file
    flag_to_draw : Flag of Showing spectogram

    return
    y: numpy array of sound data
    sr: sampling rate
    """
    name = fileName.replace('.mp3','')
    name = 'temp.wav'
    AudioSegment.from_file(fileName).export(name, format="wav", bitrate="16k")

    y, sr = lr.load(name, sr) # Loading Data
    stft_result = lr.stft(y, n_fft=n_fft, win_length=win_length, hop_length=hop_length)
    
    os.remove(name)

    if flag_to_draw :
        D = np.abs(stft_result)
        S_dB = lr.power_to_db(D, ref=np.max)

        lr.display.specshow(S_dB, sr=sr, hop_length=512,
                        y_axis='mel', x_axis='time', cmap=cm.jet)
        plt.colorbar(format='%2.0f dB')
        plt.show()

    return y, sr


# Write sound data
def write_audio(y, file_name, sr=22050, win_length=2048, hop_length=512):
    """
    y : Sound data
    dirPath, fileName : Path of file
    """
    file_path = './' + file_name
    # files
    mp3_file = os.path.abspath(file_path + '.mp3')
    wav_file = os.path.abspath(file_path + '.wav')

    sf.write(wav_file, y, sr, subtype='PCM_24')

    # convert wav to mp3
    sound = AudioSegment.from_wav(wav_file)
    sound.export(mp3_file, format="mp3") 



from spleeter.separator import Separator
from read_write_audio import read_audio
import os
from spleeter.audio.adapter import AudioAdapter

def separate_vocal(path, sr):
    separator = Separator('spleeter:2stems')
    
    audio_loader = AudioAdapter.default()
    y, sr = audio_loader.load(path, sample_rate=sr)

    prediction = separator.separate(y)
    vocal = prediction['vocals']
    audio_loader.save('./temp0.mp3',vocal,sr)
    vocals, sr = read_audio('./temp0.mp3')
    os.remove('./temp0.mp3')
    accompaniment = prediction['accompaniment']
    audio_loader.save('./temp0.mp3',accompaniment,sr)
    accompaniment, sr = read_audio('./temp0.mp3')
    os.remove('./temp0.mp3')
    return vocals, accompaniment, sr


