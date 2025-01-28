from flask import Blueprint, request
from timeit import default_timer as timer
from backend.db_functions.quiz_methods import insert_quiz_questions_in_db, fetch_questions_from_db
from backend.quiz_creator.quiz_generator import generate_quiz
from backend.db_functions.summary_methods import extract_summary_from_db, add_new_summary
from backend.db_functions.references_methods import get_references_from_db, insert_multiple_references
from backend.llm_methods.prompt_functions import generate_summary, extract_json, get_important_keywords_from_llm
from backend.functions.keyword_extraction import get_important_keywords
from backend.functions.resource_collection import get_top_resources
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

        print("Generating summary...")
        summary_text = generate_summary(subtitle_text)
        db_summary_text = add_new_summary([section_id, summary_text])
        print("Summary added to the database successfully.")
        json_data = get_summary_json(summary_text)
        return json_data

    else:
        json_data = get_summary_json(summary_text[-1])

        return json_data

@GEN_BLUEPRINT.route("/get-references")
def get_references():
    start_time = timer()

    section_id = request.args.get("section_id")
    heading_text = request.args.get("heading")
    video_id = request.args.get("video_id")
    start = request.args.get("start")
    end = request.args.get("end")

    reference_list = get_references_from_db(section_id)
    print(reference_list)
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
        topic_list = get_important_keywords(only_text)

        top_7 = topic_list[:7]

        # Get section title and course title
        query_header = get_section_title_and_course_title(section_id)


        # Pass them into script to scrape internet
        all_resources = []
        for topic in top_7:
            print(f"Getting Resources for Topic: {topic}")
            all_resources.extend(get_top_resources(query_header+topic))

        end_time = timer()
        print(f"Total Time Taken: {end_time-start_time} seconds")
        insert_multiple_references(section_id=section_id,
                                   data_list=all_resources)
        print(f"Resources added to the database successfully")
        return all_resources

    else:
        return reference_list

@GEN_BLUEPRINT.route("/fetch-questions")
def get_questions():
    course_name = request.args.get("courseName")
    video_id = request.args.get("videoID")
    start = request.args.get("startTime")
    end = request.args.get("endTime")
    section_name = request.args.get("sectionName")
    section_ID = request.args.get("sectionID")

    print(course_name, section_name, section_ID)
    quiz_questions = fetch_questions_from_db(int(section_ID))

    if(len(quiz_questions) == 0):
        # Spoken content
        subtitle_text = get_subtitles(video_id=video_id,
                                      from_seconds=int(start),
                                      to_seconds=int(end))

        print(subtitle_text)
        only_text = ""

        for obj in subtitle_text:
            only_text += obj["text"]

        # Generate new quiz
        quiz_data = generate_quiz(f"{course_name} {section_name}", only_text)

        insert_quiz_questions_in_db(section_ID, quiz_data)

        quiz_questions = fetch_questions_from_db(int(section_ID))
        return quiz_questions

    return quiz_questions

# TODO - Write a tidifying function that cleans the subtitle and presents it in a readable format. Use Gen AI for this