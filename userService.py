from user import user 
class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):
        return cls.users.pop(user_id, None) is not None

    @classmethod
    def update_user(cls, user_id, **kwargs):
        user = cls.find_user(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            return True
        return False

    @classmethod
    def get_number(cls):
        return len(cls.users)
