from flask import Blueprint, request
import re
import regex
import json
from backend.db_functions.summary_methods import extract_summary_from_db, add_new_summary
from backend.db_functions.references_methods import get_references_from_db
from backend.llm_methods.prompt_functions import generate_summary, extract_json, get_important_keywords_from_llm
from backend.functions.keyword_extraction import get_important_keywords
from backend.db_functions.section_methods import get_section_title_and_course_title
from backend.data_retrieval_methods import get_subtitles
from backend.utils.extractor import get_summary_json

GEN_BLUEPRINT = Blueprint('gen_ai', __name__)

@GEN_BLUEPRINT.route("/generate-summary")
def gen_summary():
    section_id = request.args.get("section_id")
    heading_text = request.args.get("heading")
    video_id = request.args.get("video_id")
    start = request.args.get("start")
    end = request.args.get("end")

    summary_text = extract_summary_from_db(section_id)
    print(summary_text)

    if(len(summary_text) == 0):
        subtitle_text = get_subtitles(video_id=video_id,
                                      from_seconds=int(start),
                                      to_seconds=int(end))


        summary_text = generate_summary(subtitle_text)
        db_summary_text = add_new_summary([section_id, summary_text])

        json_data = get_summary_json(summary_text)
        return json_data

    else:
        json_data = get_summary_json(summary_text[-1])

        return json_data

@GEN_BLUEPRINT.route("/get-references")
def get_references():
    section_id = request.args.get("section_id")
    heading_text = request.args.get("heading")
    video_id = request.args.get("video_id")
    start = request.args.get("start")
    end = request.args.get("end")

    reference_list = get_references_from_db(section_id)
    if(len(reference_list) == 0):
        # Generate references with Llama 3 and Selenium Script
        subtitle_text = get_subtitles(video_id=video_id,
                                      from_seconds=int(start),
                                      to_seconds=int(end))

        print(subtitle_text)
        only_text = ""

        for obj in subtitle_text:
            only_text += obj["text"]


        # Generate important topics from subtitle text
        topic_list = get_important_keywords_from_llm(only_text)

        top_10 = topic_list[:10]

        # Get section title and course title
        query_header = get_section_title_and_course_title(section_id)


        # Pass them into script to scrape internet
        print(query_header)


        # Pass the list onto the script

# TODO - Write a tidifying function that cleans the subtitle and presents it in a readable format. Use Gen AI for this