import numpy as np
import matplotlib.pyplot as plt
import librosa as lr

def delta_pitch(target, now):
    return 12 * np.log2(target / now)

def edit_pitch(data, sr, target_pitch, current_pitch):
    d = delta_pitch(target_pitch, current_pitch)
    step = np.round(d * 4)
    data = lr.effects.pitch_shift(data, sr, step, bins_per_octave = 48)

def edit_length(data, target_length, now_length):
    delta_length = now_length / target_length
    return lr.effects.time_stretch(data, delta_length)

def generate_f0(y, sr, frame_length=2048, hop_length=512, show_graph=False):
    """
    Parameters
    y: sound data
    sr: sampling rate
    frame_length: length of a frame
    hop_length: length of shifting
    show_graph: boolean if true show a graph

    return
    f0: natural frequency (n_frames, )
    voiced_flag: flag of voiced (n_frames, )
    n_frames = len(y) / hop_length
    """
    f0, voiced_flag, voiced_probs = lr.pyin(y, fmin=lr.note_to_hz('C2'), 
                                            fmax=lr.note_to_hz('C7'), sr=sr, frame_length=frame_length, hop_length=hop_length)
    if show_graph:
        times = lr.times_like(f0)
        D = lr.amplitude_to_db(np.abs(lr.stft(y, n_fft=4096, win_length=2048, hop_length=512)), ref=np.max)
        fig, ax = plt.subplots()
        img = lr.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
        ax.set(title='pYIN fundamental frequency estimation')
        fig.colorbar(img, ax=ax, format="%+2.f dB")
        ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
        ax.legend(loc='upper right')

    return f0, voiced_flag

def frame_to_samples(max_length, start_idx, end_idx, hop_length=512):
    """
    transfrom Frame index to Sample index
    """
    dur = []
    dur.append(start_idx * hop_length)
    if max_length < end_idx * hop_length + hop_length - 1:
        dur.append(max_length - 1)
    else:
        dur.append(end_idx * hop_length + hop_length - 1)

    return dur

class note:
    def __init__(self, y, f0, duration, isvoiced):
        """
        y: sound data in duration
        f0: natural frequency datas in duration
        duration: duration
        is_voiced: flag of voiced
        tone: tone info transformed from f0
        """
        self.y = y
        self.f0 = f0
        self.duration = duration
        self.is_voice = isvoiced
        self.tone = None
    
    def print(self): # print information of a note
        print('-'*70)

        print("Sound Information")
        print("Is voiced: ", self.is_voice)
        print(self.y)
        print("Shape of sound", self.y.shape)

        print("F0 Information")
        print(self.f0)
        print("Shape of f0", self.f0.shape)

        print("Duration Information")
        print(self.duration)

        print('-'*70)


class blocking:
    def __init__(self, y, sr):
        """
        notes: list of note
        y: sound data
        f0: natural frequency data
        voiced_flag: flag of voiced
        voiced_blocks: list of voiced index arrays
        unvoiced_blocks: list of unvoiced index arrays
        """
        self.notes = []
        self.y = y
        self.f0, self.voiced_flag = generate_f0(y, sr)
        self.voiced_blocks = []
        self.unvoiced_blocks = []
    
    def make_blocks(self):
        voiced_flag = self.voiced_flag
        voiced_idx = np.where(voiced_flag == True)[0]
        unvoiced_idx = np.where(voiced_flag == False)[0]

        # List of Index arrays
        voiced_list = np.split(voiced_idx, np.where(np.diff(voiced_idx) != 1)[0] + 1)
        unvoiced_list = np.split(unvoiced_idx, np.where(np.diff(unvoiced_idx) != 1)[0] + 1)

        for sound in voiced_list:
            self.voiced_blocks.append(sound)
            start_idx = sound[0] # start index of duration in frame
            end_idx = sound[len(sound) - 1] # end index of duration in frame
            dur = frame_to_samples(len(self.y), start_idx, end_idx) # duration in sample

            n = note(self.y[dur[0] : dur[1]], self.f0[start_idx : end_idx], [dur[0], dur[1]], True)
            self.notes.append(n)

        for sound in unvoiced_list:
            self.unvoiced_blocks.append(sound)
            start_idx = sound[0]
            end_idx = sound[len(sound) - 1]
            dur = frame_to_samples(len(self.y), start_idx, end_idx)

            n = note(self.y[dur[0] : dur[1]], self.f0[start_idx : end_idx], [dur[0], dur[1]], False)
            self.notes.append(n)

        self.notes = sorted(self.notes, key = lambda x : x.duration[0]) # sort by time
        return self.notes

    def print(self, start_idx, end_idx):
        print("About Notes from {0} to {1}".format(start_idx, end_idx))
        for i in range(start_idx, end_idx + 1):
            self.notes[i].print()


"""
usage
data = blocking(y, sampling_rate) full data
notes = data.make_blocks()
data.print(1, 3)
"""
