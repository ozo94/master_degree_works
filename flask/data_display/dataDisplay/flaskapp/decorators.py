# -*- coding: utf-8 -*-
"""permission required"""

from functools import wraps
from flask import abort

from flask_login import current_user


def permission_required(permissions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.check_permission(permissions):
                abort(403)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def admin_required(func):
    return permission_required(15)(func)


def minister_required(func):
    return permission_required(7)(func)


def clerk_required(func):
    return permission_required(3)(func)


def chief_required(func):
    return permission_required(1)(func)
