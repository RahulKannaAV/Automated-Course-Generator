import re
from typing import List, Dict
from dotenv import load_dotenv
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

def get_section_timestamps(description: str) -> Dict:
    pattern = r"(?P<time>(?:\d{1,3}:)*\d{1,2}:\d{1,2})[- )]*(?P<chapter>.*)"
    # Extracting matches into a dictionary
    matches = re.findall(pattern, description, re.MULTILINE)
    chapter_dict = {time: chapter for time, chapter in matches}
    print(chapter_dict)
    return chapter_dict

load_dotenv()
"""
try:
    yt_url = "https://www.youtube.com/watch?v=ix9cRaBkVe0"
    yt = YouTube(url=yt_url, on_progress_callback=on_progress)
    text = yt.description
    print(get_section_timestamps(text))
except:
    print("No Description Found")"""




