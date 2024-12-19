from youtube_transcript_api import YouTubeTranscriptApi
# from data_retrieval_methods import get_subtitles
# Use this to generate quiz
def extract_section_transcript(from_seconds, to_seconds, video_id):

    result = YouTubeTranscriptApi.get_transcript(video_id=video_id)

    subtitles = ""

    for sub in result:
        subtitleDuration = sub['start']
        if(subtitleDuration>to_seconds):
            break
        else:
            if(subtitleDuration>=from_seconds and subtitleDuration<=to_seconds):
                subtitles += sub['text'] + " "

    return subtitles

section_transcript = extract_section_transcript(video_id="gyMwXuJrbJQ",
                                      from_seconds=545,
                                      to_seconds=7276)

with open("big_lesson.txt", 'w') as f:
    f.write(section_transcript)
