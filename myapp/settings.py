import os

import pymongo

client = pymongo.MongoClient('192.168.80.128', 27017)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PHOTO_DIR = "photo"
MUSIC_DIR = "music"
FILE_DIR = "D:\Lotus\Domino\data\domino\html\mesintface"

if __name__ == '__main__':
    res = client['local']['content'].find({}, {"_id": 0})
    print(res)
    for re in res:
        print(re)
