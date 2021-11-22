from flask import (
    Flask,
    request,
    jsonify
)
from flask_jwt_extended import (
    JWTManager,
    get_jwt_identity,
    jwt_required,
    create_access_token
    
)

app = Flask(import_name=__name__)
# app.secret_key = 'inups'
app.config.update(JWT_SECRET_KET='dhkim')

jwt = JWTManager(app)

root_id = 'bigt'
root_pw = '9999'


@app.route("/")
def test():
    return "hello"


@app.route("/login", methods=["POST"])
def test_login():
    user_input = request.get_json()
    user_id = user_input['id']
    user_pw = user_input['pw']

    if (user_id == root_id) & (user_pw == root_pw):
        return jsonify({
            'result': 'login_success',
            'token': create_access_token(identity=user_id,
                                         expires_delta=False)
            })

    else:
        return jsonify({
            'result': 'invalid id/pw',
            'token': ''
            })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
