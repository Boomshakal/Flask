from flask import Blueprint, request, jsonify

from settings import client, RESPONSE

user = Blueprint('user', __name__)


@user.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


@user.route('/login', methods=['POST'])
def login():
    form_data = request.form.to_dict()
    res = client['local']['user'].find_one(form_data)

    if res:
        res['_id'] = str(res['_id'])
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
