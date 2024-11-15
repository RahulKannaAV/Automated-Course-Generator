from youtube_transcript_api import YouTubeTranscriptApi
from test import generate_quiz

result = YouTubeTranscriptApi.get_transcript("iuK05gGBzJc")

#print(result)

# Get subtitles upto Chemistry basics
from_seconds = 1334
to_seconds = 1952
subtitles = ""

for sub in result:
    subtitleDuration = sub['start']
    if(subtitleDuration>to_seconds):
        break
    else:
        if(subtitleDuration>=from_seconds and subtitleDuration<=to_seconds):
            subtitles += sub['text'] + " "

print(subtitles)

# print("Generated Quizzes")
#print(generate_quiz(subtitles))
