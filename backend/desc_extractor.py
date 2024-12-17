import re
from typing import List, Dict
from dotenv import load_dotenv
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

def get_section_timestamps(text: str) -> Dict:
    pattern = r"(?:\s*⌨️?\s*|\s*⭐️?\s*)?\(?(\d{1,2}:\d{2}(?::\d{2})?)\)?\s*[-:]*\s*(.+)"

    # Find all matches of the pattern in the text
    title_matches = re.findall(pattern, text)

    # Making dictionary from the matches
    timestamp_dict = {section[0]: section[1] for section in title_matches}

    return timestamp_dict


load_dotenv()
"""
try:
    yt_url = "https://www.youtube.com/watch?v=ix9cRaBkVe0"
    yt = YouTube(url=yt_url, on_progress_callback=on_progress)
    text = yt.description
    print(get_section_timestamps(text))
except:
    print("No Description Found")"""



