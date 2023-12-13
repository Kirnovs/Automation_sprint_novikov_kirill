import requests
import configuration
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)


def post_new_client_kit(kit_body, auth_token):
    url = configuration.URL_SERVICE + configuration.CREATE_KITS_PATH
    body = {
        "name": kit_body
    }
    new_headers = data.headers.copy()
    new_headers["Authorization"] = f"Bearer + {auth_token}"
    return requests.post(url, json=body, headers=new_headers)
