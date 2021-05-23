#import librosa as lr
#from read_write_audio import write_audio
#y, sr = lr.load('./추출.wav')
# y = lr.effects.time_stretch(y, 0.9)
# y = lr.effects.pitch_shift(y, sr, 3, bins_per_octave = 48)
# write_audio(y,'추출')

# song = [1,2,3,4,5,6,7]
# music = [1,2,3,4,5,6,7]
# out = song

# if len(song) == len(music):
#     for i in range(len(music)):
#         out[i] = song[i] + music[i]

# print(out)

# from pydub import AudioSegment
# AudioSegment.converter = "C:/Users/hiaru/Desktop/khlug/sing-in-your-voice/ffmpeg/bin/ffmpeg.exe"
# sound = AudioSegment.from_wav('./추출.wav')
# print(len(sound))
# sound.export('./ccc.mp3', format="mp3") 
#write_audio(y,'ccc')
import os

print(os.path.abspath('.'))

 # class note:
#     def __init__(self, y, f0, duration, isvoiced):
#         """
#         y: sound data in duration
#         f0: natural frequency datas in duration
#         duration: duration
#         is_voiced: flag of voiced
#         tone: tone info transformed from f0
#         """
#         self.y = y
#         self.f0 = f0
#         self.duration = duration
#         self.is_voice = isvoiced
#         self.tone = None
    
#     def print(self): # print information of a note
#         print('-'*70)

#         print("Sound Information")
#         print("Is voiced: ", self.is_voice)
#         print(self.y)
#         print("Shape of sound", self.y.shape)

#         print("F0 Information")
#         print(self.f0)
#         print("Shape of f0", self.f0.shape)

#         print("Duration Information")
#         print(self.duration)

#         print('-'*70)

#     def print_duration(self):
#         print(self.duration)
    
#     def delta_duration(self):
#         return self.duration[1]-self.duration[0]+1

#     def append(self, note, is_voice):
#         if self.duration[1] +1 == note.duration[0]:
#             self.y.extend(note.y)
#             self.f0.extend(note.f0)
#             self.duration = [self.duration[0],note.duration[1]]
#             self.is_voice = is_voice
#             return self
#         else:
#             raise Exception("can't append note!!")

# class block:
#     def __init__(self, y, sr):
#         """
#         notes: list of note
#         y: sound data
#         f0: natural frequency data
#         voiced_flag: flag of voiced
#         voiced_blocks: list of voiced index arrays
#         unvoiced_blocks: list of unvoiced index arrays
#         """
#         self.__notes = []
#         self.__y = y
#         self.__sr = sr
#         self.__f0, self.__voiced_flag = generate_f0(y, sr)
#         self.__voiced_blocks = []
#         self.__unvoiced_blocks = []
    
#     def __make_blocks(self):
#         voiced_flag = self.__voiced_flag
#         voiced_idx = np.where(voiced_flag == True)[0]
#         unvoiced_idx = np.where(voiced_flag == False)[0]

#         # List of Index arrays
#         voiced_list = np.split(voiced_idx, np.where(np.diff(voiced_idx) != 1)[0] + 1)
#         unvoiced_list = np.split(unvoiced_idx, np.where(np.diff(unvoiced_idx) != 1)[0] + 1)
#         for sound in voiced_list:
#             self.__voiced_blocks.append(sound)
#             start_idx = sound[0] # start index of duration in frame
#             end_idx = sound[len(sound) - 1] # end index of duration in frame
#             dur = frame_to_samples(len(self.__y), start_idx, end_idx) # duration in sample

#             n = note(self.__y[dur[0] : dur[1]], self.__f0[start_idx : end_idx+1], [dur[0], dur[1]], True)
#             self.__notes.append(n)

#         for sound in unvoiced_list:
#             self.__unvoiced_blocks.append(sound)
#             start_idx = sound[0]
#             end_idx = sound[len(sound) - 1]
#             dur = frame_to_samples(len(self.__y), start_idx, end_idx)

#             n = note(self.__y[dur[0] : dur[1]], self.__f0[start_idx : end_idx+1], [dur[0], dur[1]], False)
#             self.__notes.append(n)

#         self.__notes = sorted(self.__notes, key = lambda x : x.duration[0]) # sort by time
#         return self.__notes

#     def print(self, start_idx, end_idx):
#         print("About Notes from {0} to {1}".format(start_idx, end_idx))
#         for i in range(start_idx, end_idx + 1):
#             self.__notes[i].print()
           
#     def __glue_notes(self):
#         y = np.array([])
#         for note in self.__notes:
#             y = np.r_[y,note.y]
#         self.__y = y

#     def __match_duration(self, target_notes):
#         from_notes = self.__notes
#         if len(target_notes) != len(from_notes):
#             print('target')
#             print(len(target_notes))
#             print('from')
#             print(len(from_notes))
#             raise Exception('Block count mismatch!!')
#         for from_note, to_note in zip(from_notes, target_notes):
#             from_note.y = edit_length(from_note.y, from_note.duration, to_note.duration)
#             from_note.duration = to_note.duration
#         self.__notes = from_notes
    
#     def __match_pitch(self,target_notes):
#         from_notes = self.__notes
#         if len(target_notes) != len(from_notes):
#             raise Exception('Block count mismatch!!')
#         for from_note, to_note in zip(from_notes, target_notes):
#             if np.isnan(from_note.f0.all()) or np.isnan(to_note.f0.all()):
#                 from_f0 = np.mean(from_note.f0)
#                 to_f0 = np.mean(to_note.f0)
#                 from_note.y = edit_pitch(from_note.y, self.__sr, from_f0, to_f0)
#         self.__notes = from_notes
        
#     def match(self, target_y):
#         y_block = block(target_y,self.__sr)
#         y_notes = y_block.__make_blocks()
#         self.__make_blocks()
#         y_notes = self.__match_blocks(y_notes)
#         self.__match_duration(y_notes)
#         self.__match_pitch(y_notes)
#         self.__glue_notes()
#         return self.__y

#     def __match_blocks(self,target_notes):
#         l_s = len(self.__notes)
#         l_t = len(target_notes)
#         #end_p_flag = 0
#         if l_s != l_t:
#             d_l = l_s - l_t
#             flag = 0
#             if d_l > 0:
#                 long_notes = self.__notes
#                 flag = 0
#             else:
#                 long_notes = target_notes
#                 flag = 1
#             # if d_l%2 != 0:
#             #     end_p_flag = 1
#             notes = pd.DataFrame(columns=['idx', 'note', 'delta'])
#             for i, note in enumerate(long_notes):
#                 notes.append({ 'idx':i, 'note':note, 'delta':note.delta_duration() }, ignore_index=True)
#             notes.sort_values(by='delta')
#             i = 0
#             while d_l > 0:
#                 idx = notes.iloc[[i],[0]]
#                 if long_notes[idx] == 0:
#                     rear = long_notes[idx+2:]
#                     front =  long_notes[idx].append(long_notes[idx+1])
#                     long_notes = front.extend(rear)
#                     d_l = d_l - 1
#                     i = i+1
#                 elif long_notes[idx] == len(long_notes)-1:
#                     front = long_notes[:idx-2]
#                     rear =  long_notes[idx-1].append(long_notes[idx])
#                     long_notes = front.extend(rear)
#                     d_l = d_l - 1
#                     i = i+1
#                 else:
#                     front=long_notes[:idx-2]
#                     rear = long_notes[idx+2:]
#                     mid =  long_notes[idx-1].append(long_notes[idx]).append(long_notes[idx+1])
#                     front.extend(mid)
#                     long_notes = front.extend(rear)
#                     d_l = d_l - 2
#                     i = i+1
#             if flag:
#                 target_notes = long_notes
#             else:
#                 self.__notes = long_notes
#         return target_notes