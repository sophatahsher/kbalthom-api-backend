class BaseController():

    model               = None
    request_parameters  = {}

    def __int__(self):
        pass

    def setModel(self, Obj)-> None:
        self.model = Obj

    def getModel(self):
        return self.model

    def setField(self, key, value)->dict:
        self.request_parameters[key] = value

    def default_request(self)-> None:

        self.request_parameters = {
            'access_token': '1111111111111111'
        }