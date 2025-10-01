import configuration
import requests
import data


# Hace copia del body en data y le agrega el endpoint de new user
# + convierte el user_body en data en un JSON
def post_new_user(user_body):
    current_body = data.user_body.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body)


def get_users_table():
    url = configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    response = requests.get(url)
    return response
