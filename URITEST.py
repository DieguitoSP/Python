import requests
from requests import HTTPError

for url in ['http://192.168.33.10:443/IdManager/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('ID Manager 1 Success!')
for url in ['http://192.168.33.20:443/IdManager/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('ID Manager 2 Success!')
for url in ['http://192.168.33.12:10443/AuthManager/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('Auth Manager 1 Success!')
for url in ['http://192.168.33.22:10443/AuthManager/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('Auth Manager 2 Succes!')
for url in ['http://192.168.33.17:9443/ContentManager/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('Content Manager 1 Success!')
for url in ['http://192.168.33.27:9443/ContentManager/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('Content Manager 2 Success!')
for url in ['http://192.168.33.14:8443/DCMMonitor/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('DCM Monitor 1 Success!')
for url in ['http://192.168.33.24:8443/DCMMonitor/api/v1/testing']:
    try:
        response = requests.get(url)
        response.raise_for_status
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('DCM Monitor 2 Success!')
for url in ['http://192.168.33.16:8080/eventsManager/echo']:
    try:
        response = requests.get(url)
        response.raise_for_status
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as  err:
        print(f'Other error ocurred:{err}')
    else:
        print('Event Manager 1 Success!')
for url in ['http://192.168.33.26:8080/eventsManager/echo']:
    try:
        response = requests.get(url)
        response.raise_for_status
    except HTTPError as http_err:
        print(f'HTTP error ocurred:{http_err}')
    except Exception as err:
        print(f'Other error ocurred:{err}')
    else:
        print('Event Manager 2 Success!')
