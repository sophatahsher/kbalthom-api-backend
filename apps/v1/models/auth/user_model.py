from applications.system.base_model import BaseModel

class UserModel(BaseModel):

    def __int__(self, req):

        super(UserModel, self).__init__()

        self.parameters = req

    def login(self):

        return self.parameters

    def Test(self):

        return self.parameters