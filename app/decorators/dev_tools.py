from flask import abort
from flask_login import current_user
from functools import wraps


def dev_tools(func):
    @wraps(func)
    def decorador(*args, **kwargs):
        if current_user.is_authenticated and (current_user.user_role_id != 3):
            return func(*args, **kwargs)
        else:
            return abort(401)

    return decorador


def dev_tools_fetch(func):
    @wraps(func)
    def decorador(*args, **kwargs):
        if current_user.is_authenticated and (current_user.user_role_id != 3):
            return func(*args, **kwargs)
        else:
            return {"res": {"status": False, "msg": "Unauthorized access"}}

    return decorador
