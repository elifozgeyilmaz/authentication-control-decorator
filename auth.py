def require_role(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.roles != required_role:
                raise PermissionError("Forbidden")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
