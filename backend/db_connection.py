import psycopg2
import os
import datetime
from dotenv import load_dotenv
from typing import Tuple, List, Dict

load_dotenv()
conn = psycopg2.connect(database=os.environ['DATABASE'],
                        user=os.environ['USER'],
                        host=os.environ['HOST'],
                        password=os.environ['PASSWORD'],
                        port=os.environ['PORT'])
