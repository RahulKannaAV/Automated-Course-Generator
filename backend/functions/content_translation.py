import sys
sys.path.append("../..")
from backend.subtitles import extract_section_transcript
from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('hello my dear kutty chaathaans. Intha traffic vera', lang='en')
tts.write_to_fp(mp3_fp)
