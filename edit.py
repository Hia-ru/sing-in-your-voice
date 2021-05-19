import librosa
import numpy as np

# 목표피치 -현재피치
def delta_P(target, now):
    return 12*np.log2(target/now)

# 피치보정
def edit_P(data,sr,target_P,now_P):
    D = delta_P(target_P, now_P)
    step = np.round(D*4)
    data = librosa.effects.pitch_shift(data,sr,step,bins_per_octave = 48)

def edit_L(data,target_L,now_L):
    delta_L = now_L/target_L
    return librosa.effects.time_stretch(data,delta_L)

notes = []

# def block(data):
#     sp = librosa.effects.split(data)
#     for
#         #무음처리
#         class note:
#             data
#             f0
#             beat
#         notes.push(note)
#         #음처리
#         class note:
#             data
#             f0
#             beat
#         notes.push(note)