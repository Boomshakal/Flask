import hashlib
import os
import time
import uuid

import requests
from flask import Blueprint

from settings import BASE_DIR, QR_DIR, client

QR = Blueprint('QR', __name__)


@QR.route('/createQR')
def createQR():
    url = 'http://qr.liantu.com/api.php?text={text}'
    code_str = str(uuid.uuid4()) + str(time.time())
    code = hashlib.md5(code_str.encode('UTF-8')).hexdigest()
    print(code)

    res = requests.get(url.format(text=code))
    # print(res.content)
    file_path = os.path.join(BASE_DIR, QR_DIR, code)
    with open(file_path + '.png', 'wb') as f:
        f.write(res.content)

    insert_res = client['local']['QR'].insert_one({'code': code})
    return str(insert_res.inserted_id)
