from flask import request, jsonify
from applications.system.base_controller import BaseController
from apps.v1.models.auth.user_model import UserModel

class UserController(BaseController):

    def __init__(self):

        super(UserController, self).__init__()

        self.default_request()

        self.setModel(UserModel(self.request_parameters))

    def login(self):

        try:
            _request = request.get_json(silent=True)
            print('login============', _request)

            # set params
            self.setField('username', _request.get('username') or '')

            #res = self.getModel().Test()

            return jsonify(message='Welecome to API section!'), 200


        except Exception as e:
            print(e)