import librosa
import numpy as np

SEMITONe = np.


# 목표피치 -현재피치
def delta_P(target, now):
    return 12*np.log2(target/now)

# 목표길이 -현재길이
def delta_L(target, now):
    return now/target

# 피치보정
def edit_P(data,sr,target_P,now_P):
    D = delta_P(target_P, now_P)
    step = np.round(D*4)
    data = librosa.effects.pitch_shift(data,sr,step,bins_per_octave = 48)




#voco = librosa.effects.time_stretch(sig,0.5)