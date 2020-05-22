from flask import Blueprint, jsonify, send_file, make_response

from database_connect import Parameters, DatabasePool
from settings import BASE_DIR, PHOTO_DIR, MUSIC_DIR, FILE_DIR
import os

gsa = Blueprint('gsa', __name__)


@gsa.route('/get_photo/<file_name>')
def get_photo(file_name):
    file_path = os.path.join(BASE_DIR, PHOTO_DIR, file_name)
    print(file_path)
    return send_file(file_path)


@gsa.route('/get_music/<file_name>')
def get_music(file_name):
    file_path = os.path.join(BASE_DIR, MUSIC_DIR, file_name)

    return send_file(file_path)


@gsa.route('/get_file/<file_name>')
def get_file(file_name):
    sql = '''
        EXEC p_mes_get_iqcdoc_from @code
        '''

    p = Parameters().add('code', file_name)

    connect = DatabasePool('mssql')
    lists = connect.ExecuteQueryAsync(sql, p)
    for list in lists:
        file_path = os.path.join(FILE_DIR, list.get('attachunid'), list.get('Attachments'))
        print(file_path)

        response = make_response(send_file(file_path))
        return response
