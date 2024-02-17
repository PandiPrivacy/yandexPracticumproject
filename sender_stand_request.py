import configuration
import requests


def post_new_client_kit(kit_body, auth):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers={'Authorization': 'Bearer '+auth,'Content-Type': 'application/json'})