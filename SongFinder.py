import sys
from acrcloud.recognizer import ACRCloudRecognizer


#Add your arc API credentials in the config

config = {
    'host':'',
    'access_key':'',
    'access_secret':'',
    'timeout':10
}

def findTheSong(filename):
    re = ACRCloudRecognizer(config)
    return re.recognize_by_file(filename, 0)
