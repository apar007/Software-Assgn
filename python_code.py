import os
import random
from playsound import playsound

# Set the directory where your audio files are stored
audio_dir = 'C:/Users/Swapnali P/Desktop/Apar'

# Getting names of audio files
audio_files = [os.path.join(audio_dir, file) for file in os.listdir(audio_dir) if file.endswith('.mp3')]

while(1):
    #Shuffling audio
    random.shuffle(audio_files)
    #Playing audio
    for i in audio_files:
        playsound(i)

exit()
