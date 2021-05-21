def vocal_extract (vocal,sr) #그냥 무시

1차시도

def audio_analysis(self,path,name):
	audio, sampling_rate = librosa.load(path,mono=True)
	sum = 0
	count = 0 
	arr = []
	blocks = 270
	one_block_data = int(len(audio)/270)
	w = open(path+".txt",'w')
	for element in audio:
		count+=1
		sum+=abs(element)
		if(count>=one_block_data):
			data = int(round(((sum)/one_block_data),3)*300)
			arr.append(data)
			count = 0
			sum = 0
			w.write(str(data)+"\n")
		print(arr)
		w.close()

2차시도

def vocal_extract(wav_file)
	#MFCC
	y,sr = librosa.load(wav_file, sr=16000)  

	# wav_length = len(y)/sr
	input_nfft = int(round(sr*frame_length))
	input_stride = int(round(sr*frame_stride))

	S = liborsa.feature.MFCC(y=y, n_mels=40, n_fft=input_nftt, hop_length=input-stride)

	print("Wav length: {}, MFCC shape:{}".format(len(y)/sr,np.shape(S)))