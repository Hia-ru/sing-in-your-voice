import librosa as lr
import numpy as np

def vocal_extract(y,sr):
	#MFCC 
	# wav_length = len(y)/sr
	input_nfft = int(round(sr*frame_length))
	input_stride = int(round(sr*frame_stride))

	S = lr.feature.MFCC(y=y, n_mels=40, n_fft=input_nfft, hop_length=input_stride)

	print("Wav length: {}, MFCC shape:{}".format(len(y)/sr,np.shape(S)))
