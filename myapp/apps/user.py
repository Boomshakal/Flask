from flask import Blueprint, request, jsonify

from settings import client, RESPONSE

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login():
    form_data = request.form.to_dict()
    res = client['local']['user'].find_one(form_data)
    res['_id'] = str(res['_id'])
    if res:
        RESPONSE['code'] = 0
        RESPONSE['msg'] = '登录成功'
        RESPONSE['data'] = res
    else:
        RESPONSE['code'] = 1
        RESPONSE['msg'] = '输入的账号或密码有误'

    return jsonify(RESPONSE)


@user.route('/register', methods=['POST'])
def register():
    form_data = request.form.to_dict()
    print(form_data)
    res = client['local']['user'].insert_one(form_data)

    RESPONSE['code'] = 0
    RESPONSE['msg'] = '注册成功'
    RESPONSE['data'] = {'user_id': str(res.inserted_id)}

    return jsonify(RESPONSE)
