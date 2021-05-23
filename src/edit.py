import numpy as np
import librosa as lr

def delta_pitch(target, now):
    return 12 * np.log2(target / now)

def edit_pitch(data, sr, current_pitch, target_pitch):
    d = delta_pitch(target_pitch, current_pitch)
    step = np.round(d * 4)
    if np.abs(step)> 48:
        step = (step/np.abs(step))*48
    return lr.effects.pitch_shift(data, sr, step, bins_per_octave = 48)

def edit_length(data, now_len, target_len):
    target_length = target_len + 1
    now_length = now_len + 1
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
                                            fmax=lr.note_to_hz('C7'), sr=sr, frame_length=frame_length, hop_length=hop_length,fill_na =1)
    if show_graph:
        times = lr.times_like(f0)
        D = lr.amplitude_to_db(np.abs(lr.stft(y, n_fft=4096, win_length=2048, hop_length=512)), ref=np.max)
        fig, ax = plt.subplots()
        img = lr.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
        ax.set(title='pYIN fundamental frequency estimation')
        fig.colorbar(img, ax=ax, format="%+2.f dB")
        ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
        ax.legend(loc='upper right')

    return f0

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

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
