from .models import User
from ariadne import convert_kwargs_to_snake_case

def listUsers_resolver(obj, info):
    try:
        users = [user.to_dict() for user in User.query.all()]
        print(users)
        payload = {
            "success": True,
            "users": users
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getUser_resolver(obj, info, user_id):
    try:
        user = User.query.get(user_id)
        print(user)
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except AttributeError:  
        payload = {
            "success": False,
            "errors": ["Post item matching {user_id} not found"]
        }
    return payload