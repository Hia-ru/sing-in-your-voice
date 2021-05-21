import librosa as lr

def vocal_extract(path):
	#MFCC 
	# wav_length = len(y)/sr
	frame_length = 0.025
	frame_stride = 0.01
	input_nfft = int(round(sr*frame_length))
	input_stride = int(round(sr*frame_stride))

	S = lr.feature.mfcc(y=y, n_mels=40, n_fft=input_nfft, hop_length=input_stride)
	return S
	

from read_write_audio import read_audio

y,sr = read_audio('./res/2.mp3')
S = vocal_extract(y,sr)
print('1')
print(S)
