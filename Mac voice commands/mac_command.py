import struct
import wave
import pvrhino
from pvrecorder import PvRecorder
import os

rhino = None
recorder = None
wav_file = None

rhino = pvrhino.create(
   access_key='YOUR_KEY',
   context_path='YOUR_Context.rhn_FILE',
   model_path='YOUR_Language.pv_FILE'
)
recorder = PvRecorder(device_index=0, frame_length=rhino.frame_length)
recorder.start()

wav_file = wave.open('PATH_TO_FILE_AUDIO/FILE_NAME', "w") 
wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))

try:
    while True:
        pcm = recorder.read()

        if wav_file is not None:
            wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))

        is_finalized = rhino.process(pcm)
        if is_finalized:
            inference = rhino.get_inference()
            if inference.is_understood:

                if inference.intent == 'Cattura': #replace the string with your command(It's better to use commands consisting of at least two words)
                    os.system('screencapture /Users/USER_NAME/Desktop/screen.png')

                if inference.intent == 'Luce_su':
                    os.system(""" osascript -e 'tell application "System Events"' -e 'key code 144' -e ' end tell' """)

                if inference.intent == 'Luce_giu':
                    os.system(""" osascript -e 'tell application "System Events"' -e 'key code 145' -e ' end tell' """)

                if inference.intent == 'Mute':
                    os.system(""" osascript -e "set volume with output muted" """)

                if inference.intent == 'Unmute':
                    os.system(""" osascript -e "set volume without output muted" """)

except KeyboardInterrupt:
    recorder.stop()
    rhino.delete()
    recorder.delete()
    wav_file.close()
    

      
