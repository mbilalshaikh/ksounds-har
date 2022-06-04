#%%
#imports
import glob as glob 
import subprocess
import pathlib
from unicodedata import category
import librosa
import matplotlib.pyplot as plt
import librosa.display
import os 
import shutil
from tqdm.notebook import trange, tqdm
import logging

# Check nvcc version
!nvcc -V
# Check GCC version
!gcc --version


#%%
# get list of k400 train files 
k400train_path = '/mnt/bdata/Data/bilal_data/mmaction_data/kinetics400/videos_train'
k400train_files = glob.glob('/mnt/bdata/Data/bilal_data/mmaction_data/kinetics400/videos_train'+'/*/*.mp4')

#%%
#functions
def create_path(wav_filepath):
    path = wav_filepath.replace(wav_filepath.split('/')[-1],'')
    p = pathlib.Path(path)
    p.mkdir(parents=True, exist_ok=True)
    print(path)

#%%
ksounds = 'blowing nose, bowling, chopping wood, ripping paper, shuffling cards, singing, tapping pen, typing, blowing out, dribbling ball, laughing, mowing the lawn by pushing lawnmower, shoveling snow, stomping, tap dancing, tapping guitar, tickling, fingerpicking, patting, playing accordion, playing bagpipes, playing bass guitar, playing clarinet, playing drums,playing guitar, playing harmonica, playing keyboard, playing organ, playing piano, playing saxophone, playing trombone, playing trumpet, playing violin, playing xylophone'
ksounds = ksounds.replace(', ',',')
ksounds = ksounds.split(',')

ksounds_dict = { i : ksounds[i] for i in range(0,len(ksounds)) }
print(ksounds_dict)


#%%
# get ksounds train folder the destination
ksoundstrain_path = '/mnt/bdata/Data/bilal_data/mmaction_data/ksounds/train'
# loop through k400 train 
classes = []
selected_files = []
for file in k400train_files:
    # extract class name 
    class_name = file.split('/')[-2]
    classes.append(class_name)
    #print(class_name)    
    # check if the class name is same as ksounds 

    if class_name in ksounds:
        # if yes : copy that into same folder in ksounds        
        ctr = ctr +1
        selected_files.append(file)
        # create destination file path         
        
        

        
    
    # else : just pass
    

    #break

# for classes in ksounds 
# extract wav file
#k400train_files[0]#,ksounds
len(set(classes))
# %%


ctr = 0 
for f in selected_files:
    dest = f.replace('kinetics400','ksounds')
    dest = dest.replace('videos_train','train')
    print(f,dest)
    #create_path(dest)
    #shutil.copy(f,dest)    
    print(ctr)
    break
    
    
# %%
audio_path = '/mnt/bdata/Data/bilal_data/ksounds_wav/train'
video_path = '/mnt/bdata/Data/bilal_data/mmaction_data/ksounds/train'

audio_files=glob.glob(audio_path+'/*/*.wav')
video_files=glob.glob(video_path+'/*/*.mp4')

a_files = []
for i in audio_files:
    print(i.split('/')[-1].split('.')[0])
    a_files.append(i.split('/')[-1].split('.')[0])
    

v_files = []
for j in video_files:
    print(j.split('/')[-1].split('.')[0])
    v_files.append(j.split('/')[-1].split('.')[0])

#%%
s_files = []
for v in v_files:
    if v not in a_files:
        s_files.append(v)
        # for abs_vid in video_files:
        #     v_name = abs_vid.split('/')[-1].split('.')[0] 
        #     if v == v_name:
        #         print(v)
        #         print(v_name)
        #         print(abs_vid)
        #         os.remove(abs_vid)
        #         break

#%%
for i in video_files:
    for j in s_files:
        if i.find(j) == -1:
            print('')
        else:
            print('it\'s here')
        
        #print(i)
        #print(j)
        

# %%
#creating annotation file

train_path = '/mnt/bdata/Data/bilal_data/mmaction_data/ksounds/rawframes_train/'
val_path = '/mnt/bdata/Data/bilal_data/mmaction_data/ksounds/rawframes_val'

f = open('ksounds27-train.txt','w')

cats = glob.glob(train_path+'/*')

for cat in cats:
    files_of_cat = glob.glob(cat+'/*')
    
    print(files_of_cat)
    for a_file in files_of_cat:
        #get file id
        file_id = str(a_file.split('/')[-1])
        #get number of frames in each file
        nb_frames = str(len(glob.glob(a_file+'/*')))
        #get class of the file
        cls_name = a_file.split('/')[-2]
        #get the class index of the file
        cls_idx = str(list(ksounds_dict.values()).index(cls_name))
        f.write(cls_name+'/'+file_id+' '+ nb_frames + ' ' + cls_idx+'\n')
        
#%%
f = open('ksounds27-val.txt','w')

cats = glob.glob(val_path+'/*')

for cat in cats:
    files_of_cat = glob.glob(cat+'/*')
    
    #print(files_of_cat)
    for a_file in files_of_cat:
        #get file id
        file_id = str(a_file.split('/')[-1])
        #get number of frames in each file
        nb_frames = str(len(glob.glob(a_file+'/*')))
        #get class of the file
        cls_name = a_file.split('/')[-2]
        #get the class index of the file
        cls_idx = str(list(ksounds_dict.values()).index(cls_name))
        f.write(cls_name+'/'+file_id+' '+ nb_frames + ' ' + cls_idx+'\n')



