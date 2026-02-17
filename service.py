from auth import require_role

class User:
    def __init__(self, roles):
        self.roles = roles  # list of roles

@require_role("admin")
def delete_user(user, user_id):
    return f"user {user_id} deleted"
