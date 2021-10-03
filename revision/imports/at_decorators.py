import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


#  @make_secure on top of a fn definition, that will prevent the fn from being created as is, and instead it will create it and pass it through the decorator in one go.
@make_secure
def get_admin_password():
    return "1234"


# user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())
