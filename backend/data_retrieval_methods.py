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

    # print(result)


    subtitles = []

    for sub in result:
        subtitleDuration = sub['start']
        textDuration = int((sub['duration']-1)*1000)
        if (subtitleDuration > to_seconds):
            break
        else:
            if (subtitleDuration >= from_seconds and subtitleDuration <= to_seconds):
                subtitles.extend([sub['text'], textDuration])
    return(subtitles)

def get_section_timestamps(description_text: str) -> Dict:
    pattern = r"(?:\(|⌨️?\s*)?(\d{1,2}:\d{2}:\d{2})(?:\)?:?\s+)(.+)"

    # Find all matches of the pattern in the text
    title_matches = re.findall(pattern, description_text)

    # Making dictionary from the matches
    timestamp_dict = {section[0]: section[1] for section in title_matches}

    return timestamp_dict

# Function to retrieve description from a Youtube video with the help of video ID
def get_youtube_description_text(video_id: str)->str:
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(url=yt_url, on_progress_callback=on_progress)
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

        section_dict["section_completion"] = False

        section_list.append(section_dict)

    return section_list


timeframe_to_seconds("01:26:56")








# ----------- EXPERIMENTATION  ----------------------
"""video_id = "F0GQ0l2NfHA"
# Get subtitles upto Chemistry basics
from_seconds = 1334
to_seconds = 1952
result = get_subtitles(video_id, from_seconds, to_seconds)
desc = get_youtube_description_text(video_id)

timestamps = get_section_timestamps(desc)

print(f"Timestamps of Video {video_id}: {timestamps}")"""