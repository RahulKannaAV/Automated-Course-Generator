from enum import Enum
from selenium.webdriver.common.by import By

class ContentID(Enum):
    CLASS = By.CLASS_NAME
    ID = By.ID
    TAG_NAME = By.TAG_NAME
    XPATH = By.XPATH
    CSS_SELECTOR = By.CSS_SELECTOR

