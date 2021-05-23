#import librosa as lr
#from read_write_audio import write_audio
#y, sr = lr.load('./추출.wav')
# y = lr.effects.time_stretch(y, 0.9)
# y = lr.effects.pitch_shift(y, sr, 3, bins_per_octave = 48)
# write_audio(y,'추출')

# song = [1,2,3,4,5,6,7]
# music = [1,2,3,4,5,6,7]
# out = song

# if len(song) == len(music):
#     for i in range(len(music)):
#         out[i] = song[i] + music[i]

# print(out)

# from pydub import AudioSegment
# AudioSegment.converter = "C:/Users/hiaru/Desktop/khlug/sing-in-your-voice/ffmpeg/bin/ffmpeg.exe"
# sound = AudioSegment.from_wav('./추출.wav')
# print(len(sound))
# sound.export('./ccc.mp3', format="mp3") 
#write_audio(y,'ccc')
import os

print(os.path.abspath('.'))

 