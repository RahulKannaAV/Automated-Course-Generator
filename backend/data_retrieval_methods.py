import re
from youtube_transcript_api import YouTubeTranscriptApi
from typing import List, Dict
from dotenv import load_dotenv
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
load_dotenv()


# Function to extract video ID from input URL
def get_video_id(video_url: str):
    video_id = ""
    pattern = r"[?&]v=([^&]+)"

    match = re.search(pattern, video_url)
    if match:
        video_id = match.group(1)
    return(video_id)

# Function to get subtitles of particular timeframe
# use this to showcase subtitles, npm install react-type-animation
def get_subtitles(video_id: str,
                  from_seconds: int,
                  to_seconds: int):


    result = YouTubeTranscriptApi.get_transcript(video_id)


    subtitles = []
    id = 0
    for sub in result:
        sentenceDict = dict()
        subtitleDuration = sub['start']
        textDuration = int((sub['duration']))
        subtitleEnd = subtitleDuration + textDuration
        if (subtitleDuration > to_seconds):
            break
        else:
            if (subtitleDuration >= from_seconds and subtitleDuration <= to_seconds):
                sentenceDict['text'] = sub['text']
                sentenceDict['start'] = subtitleDuration
                sentenceDict['end'] = subtitleEnd
                sentenceDict['id'] = id
                id += 1

                subtitles.append(sentenceDict)
    return(subtitles)

def get_section_timestamps(description_text: str) -> Dict:
    pattern = r"(?:\(|⌨️?\s*)?(\d{1,2}:\d{2}:\d{2})(?:\)?:?\s+)(.+)"

    # Find all matches of the pattern in the text
    title_matches = re.findall(pattern, description_text)

    # Making dictionary from the matches
    timestamp_dict = {section[0]: section[1] for section in title_matches}
    print(f"Section Dict: {timestamp_dict}")
    return timestamp_dict

# Function to retrieve description from a Youtube video with the help of video ID
def get_youtube_description_text(video_id: str)->str:
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(url=yt_url, on_progress_callback=on_progress, use_po_token=True)
    stream = yt.streams.first()
    text = yt.description
    return text

def timeframe_to_seconds(timeframe_string: str):
    parts = timeframe_string.split(":")[::-1]
    total_seconds = 0

    for idx, part in enumerate(parts):
        total_seconds += int(part)*(60**idx)
    return(total_seconds)

def prepare_section_list(course_id: int,
                         timestamps: Dict):
    section_list = []

    all_sections = list(timestamps.keys())
    for idx in range(len(all_sections)-1):
        section_dict = dict()

        # Section Course ID
        section_dict["course_id"] = course_id

        # Section start time
        section_dict["section_start"] = timeframe_to_seconds(all_sections[idx])

        # Section End time
        section_dict["section_end"] = timeframe_to_seconds(all_sections[idx+1])

        # Section Title
        section_dict["section_name"] = timestamps[all_sections[idx]]

        section_dict["section_completed"] = False

        section_list.append(section_dict)

    return section_list


timeframe_to_seconds("01:26:56")


data = """
⭐️ Contents ⭐️
00:00:00 Introduction & Learning Resources
00:06:19 Variables
00:27:07 Numbers & Binary System
01:09:51 Chars, Bools & Unit Types
01:17:55 Statements & Expressions
01:24:50 Functions
01:32:53 Ownership
02:24:06 Borrowing
02:47:45 String vs. &str
03:17:59 Slices
03:31:35 Tuples
03:40:04 Structs
04:02:52 Enums
04:13:46 The "Option" Enum
04:21:32 Flow Control
04:44:43 Pattern Match
05:16:42 Methods & Associated Functions
05:31:50 Generics
06:06:32 Traits
06:47:15 Trait Objects
07:09:51 Associated Types
07:39:31 String
07:59:52 Vectors
08:29:00 HashMaps
08:52:45 Type Coercion
09:04:54 From & Into
09:36:03 panic!
09:44:56 Result
10:28:23 Cargo, Crates & Modules
11:08:28 Debug & Display
11:30:13 Lifetimes
12:14:46 Lifetime Elision
12:38:53 Closures
13:30:08 Iterators"""


# ----------- EXPERIMENTATION  ----------------------
"""video_id = "F0GQ0l2NfHA"
# Get subtitles upto Chemistry basics
from_seconds = 1334
to_seconds = 1952
result = get_subtitles(video_id, from_seconds, to_seconds)
desc = get_youtube_description_text(video_id)

timestamps = get_section_timestamps(desc)

print(f"Timestamps of Video {video_id}: {timestamps}")"""
