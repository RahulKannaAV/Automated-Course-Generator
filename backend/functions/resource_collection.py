import logging
import time
import re
from typing import List
import ollama
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from enums.content_id import ContentID

def get_top_resources(query, data):
    query_string = "+".join(query.split(" "))

    WEBDRIVER_URL = r"..\chromedriver-win64\chromedriver.exe"
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(service=Service(driver_path_env_key=WEBDRIVER_URL),
                              options=options)

    driver.get(f"https://www.google.com/search?q={query_string}")
    website_titles = []
    website_links = []

    by_content = ContentID(data['contentID']).value

    try:
        targeted_elements = driver.find_elements(by_content, "h3[class='LC20lb MBeuO DKV0Md']")

        for element in targeted_elements:
            website_titles.append(element.text)

    except (exceptions.NoSuchElementException, exceptions.ElementNotInteractableException) as e:
        logging.error(f"Element doesn't exist/non-interactable {e}")


    try:
        targeted_elements = driver.find_elements(By.CSS_SELECTOR, "a[jsname='UWckNb']")

        for element in targeted_elements:
            website_links.append(element.get_attribute("href"))
    except (exceptions.NoSuchElementException, exceptions.ElementNotInteractableException) as e:
        logging.error(f"Element links doesn't exist/non-interactable {e}")

    link_dict = {website_titles[i]:website_links[i] for i in range(3)}
    return(link_dict)

def get_important_entities(text: str)->List[str]:
    ollama.pull('llama3')
    response = ollama.chat(model='llama3', messages=[
      {
        'role': 'user',
        'content': f'Print out list of 5 important entities mentioned in this text as python list, "{text}"',

      },
      ], stream=True)

    results = ""
    for chunk in response:
      print(chunk['message']['content'], end='', flush=True)
      results += chunk['message']['content']

    matches = re.findall(r'\[(.*?)\]', results)

    # print(results)
    entity_list = matches[0].split(",") if len(matches) > 0 else []

    return entity_list

"""content = ""
with open("big_lesson.txt", 'r') as f:
    for line in f.readlines():
        content += line

entities = get_important_entities(content)


print(entities)"""


