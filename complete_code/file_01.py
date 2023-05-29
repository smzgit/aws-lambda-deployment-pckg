import requests
import time


def ping_endpoint(endpoint) -> bool:
    resp = False
    try:
        resp = requests.get(url=endpoint)
        if resp.status_code == 200:
            resp = True
    except Exception as ex:
        print(f'Error while getting response from {endpoint}, Error : {ex}')
    return resp


if __name__ == '__main__':
    url = 'https://www.goo1gle.com/'
    for _ in range(5):
        response = ping_endpoint(endpoint=url)
        print(f'Ping response from {url} => {response}')
        time.sleep(1)
