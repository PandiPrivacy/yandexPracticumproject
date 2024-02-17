import configuration
import requests
import data


def post_new_client_kit(kit_body, auth):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers={'Authorization': 'Bearer '+auth,'Content-Type': 'application/json'})


def get_new_user_token():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers={'Content-Type': 'application/json'} )