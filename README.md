쿠러그 2021 1학기 파이썬 교육 팀프로젝트 '음치 보정 프로그램' 깃허브 저장소입니다.  
이 파일 확인하신 분은 아래에 이름 적어주세요.

- 구자웅
- 허진석
- 박연수
- 송인혁
- 노현

# 수정 전 test.py 내용 

+ 내용 이해하면서 작성하려고 하느라 README.md 로 옮겼습니다.
+ sig, sr = librosa.load(audio_path)
+ sig = sig[:round(len(sig)/8)]

+ time = np.linspace(0, len(sig)/sr, len(sig))

+ + STFT -> spectrogram
+ hop_length = 512  + 전체 frame 수
+ n_fft = 2048  + frame 하나당 sample 수

+ calculate duration hop length and window in seconds
+ hop_length_duration = float(hop_length)/sr
+ n_fft_duration = float(n_fft)/sr

+ + STFT
+ stft = librosa.stft(sig, n_fft=n_fft, hop_length=hop_length)
+ + print(stft[0])
+ + 복소공간 값 절댓값 취하기
+ magnitude = np.abs(stft)
+ + print(type(magnitude))
+ + magnitude >> Decibels
+ log_spectrogram = librosa.amplitude_to_db(magnitude)
+ + print(max(log_spectrogram[0]))


+ for i in range(0,100):
+     print(max(log_spectrogram[i]))

+ +display spectrogram
+ FIG_SIZE = (15, 10)
+ plt.figure(figsize=FIG_SIZE)
+ librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
+ plt.xlabel("Time")
+ plt.ylabel("Frequency")
+ plt.colorbar(format="%+2.0f dB")
+ plt.title("Spectrogram (dB)")
+ plt.show()
