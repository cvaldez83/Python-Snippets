# 1st method: auto-plays with no window popup
import winsound
winsound.PlaySound('filename',winsound.SND_FILENAME)

# 2nd method: Windows media player pops up & auto-plays
import os
os.system('filename.wav &') # & is to auto-play
