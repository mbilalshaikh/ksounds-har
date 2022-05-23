import glob as glob 
import subprocess
import pathlib



ksounds_path = '/mnt/bdata/Data/bilal_data/ksounds/'
ksounds_wavpath = '/mnt/bdata/Data/bilal_data/ksounds_wav/'


def create_path(wav_filepath):
    path = wav_filepath.replace(wav_filepath.split('/')[-1],'')
    p = pathlib.Path(path)
    p.mkdir(parents=True, exist_ok=True)
    #print(path)


def gen_wav(src,dest):
    #print(src)
    command = "ffmpeg -i '"+src+"' -ab 160k -ac 2 -ar 44100 -vn '"+dest+"'"
    subprocess.call(command,shell=True)

def generate_wav():
    files = glob.glob(ksounds_path+'*/*/*.mp4')

    for f in files:
        mp4_filepath = f
        wav_filepath = mp4_filepath.split('ksounds')[0]+'ksounds_wav'+mp4_filepath.split('ksounds')[1].split('.')[0]+'.wav'
        #print(mp4_filepath)
        #print(wav_filepath)

        create_path(wav_filepath)
        gen_wav(mp4_filepath,wav_filepath)
    len(files)

def main():
    generate_wav()

    mp4_files = glob.glob(ksounds_path+'*/*/*.mp4')
    wav_files = glob.glob(ksounds_wavpath+'*/*/*.wav')
    print(len(mp4_files), len(wav_files))

if __name__ == '__main__':
    main()