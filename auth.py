import bcrypt
from models import Admin

class Auth:
    @staticmethod
    def set_password(user, password):
        user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    @staticmethod
    def set_admin(admin_instance, password):
        admin_instance.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def check_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)    
   