import os
import random
import string
from datetime import datetime

def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def getCurrentMilliseconds():
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliSeconds = round(seconds * 1000)
    return milliSeconds

def removeFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)