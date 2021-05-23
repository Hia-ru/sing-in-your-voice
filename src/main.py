from read_write_audio import *
from edit import *
from multiprocessing import freeze_support
import glob

def search_mp3():
    mp3_list = list(glob.glob('./*.mp3'))
    out = mp3_list
    for i, mp3 in enumerate(mp3_list):
        out[i] = mp3.replace('.\\','').replace('.mp3','')
    return mp3_list

def read_wav(fileName, sr=22050):
    y, sr = lr.load(fileName, sr) # Loading Data
    return y, sr

def main():
    while True:
        freeze_support()
        # exe가 있는 폴더의 mp3 리스트 출력
        mp3_list = search_mp3()
        print('\n---- MP3 List ----')
        for mp3 in mp3_list:
            print(mp3)

        # 원본음원 입력
        while True:
            origin = input('input original song file: ').rstrip('.mp3')
            if not origin in mp3_list:
                print('Please re-enter')
                continue
            break

        # 노래음원 입력
        while True:
            song = input('input your song file: ').rstrip('.mp3')
            if not song in mp3_list:
                print('Please re-enter')
                continue
            break
        name = song

        # 음원 로딩
        print('\nloading and extracting vocal...\n')
        song, sr = read_wav(song+'.mp3')
        origin, music, sr = separate_vocal(origin+'.mp3',sr)
        
        # 보정
        print('\ncalibrating audio...')
        print('    edit length...')
        song = edit_length(song,len(song),len(origin))

        print('    generate f0...')
        f0_s = generate_f0(song, sr)
        f0_o = generate_f0(origin, sr)

        print('    chunking...')
        size = 2048
        song = list_chunk(song,size)
        #origin = list_chunk(origin,size)
        #f0_s = list_chunk(f0_s,size)
        #f0_o = list_chunk(f0_o,size)

        print('    edit pitch...')
        out = []
        for i, s in enumerate(song):
            out.extend(edit_pitch(s, sr, np.mean(f0_s[4*i:4*(i+1)]), np.mean(f0_o[4*i:4*(i+1)])))

        print('    Postprocessing...')
        if len(out) == len(music):
            for i in range(len(music)):
                out[i] = out[i]*5 + music[i]
        else:
            print(len(out))
            print(len(music))

        # 저장
        name = name+'(수정됨)'
        write_audio(out,name)
        print('\nAll completed. saved as '+name)

if __name__ == '__main__':
    main()
