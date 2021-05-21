
def vocal_extract(wav_file)
	#MFCC
	y,sr = librosa.load(wav_file, sr=16000)  

	# wav_length = len(y)/sr
	input_nfft = int(round(sr*frame_length))
	input_stride = int(round(sr*frame_stride))

	S = liborsa.feature.MFCC(y=y, n_mels=40, n_fft=input_nftt, hop_length=input-stride)

	print("Wav length: {}, MFCC shape:{}".format(len(y)/sr,np.shape(S)))
