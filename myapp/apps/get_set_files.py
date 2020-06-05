from flask import Blueprint, jsonify, send_file, make_response, request, render_template

from database.database_connect import Parameters, DatabasePool
from settings import BASE_DIR, PHOTO_DIR, MUSIC_DIR, FILE_DIR, PDF_DIR
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


@gsa.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    file_obj = request.files.get("file")  # "file"对应前端表单name属性

    print(request.form.get('string_key'))
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"

    # 将文件保存到本地
    # # 1. 创建一个文件
    # f = open("./demo.png", "wb")
    # # 2. 向文件写内容
    # data = file_obj.read()
    # f.write(data)
    # # 3. 关闭文件
    # f.close()

    # 直接使用上传的文件对象保存
    file_name = file_obj.filename
    print(file_name)
    file_path = os.path.join(BASE_DIR, PDF_DIR, file_name)
    file_obj.save(file_path)
    return "上传成功"


@gsa.route('/download/<file_name>', methods=['GET'])
def download(file_name):
    file_path = os.path.join(BASE_DIR, PDF_DIR, file_name)

    return send_file(file_path)
