from read_write_audio import *
from edit import block
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
        print('\ncalibrating audio...\n')
        song = block(song, sr)
        song = song.match(origin)

        out = song
        if len(origin) == len(music):
            for i in range(len(music)):
                out[i] = origin[i] + music[i]
        else:
            print(len(song))
            print(len(music))

        # 저장
        name = name+'(수정됨)'
        write_audio(out,name)
        print('\nAll completed. saved as '+name)

if __name__ == '__main__':
    main()
