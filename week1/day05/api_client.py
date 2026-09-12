import requests

try:

    response = requests.get(
        "https://httpbin.org/get",
        timeout=10
    )

    response.raise_for_status()

    print(response.json())

except requests.exceptions.RequestException as error:

    print(f"Request failed: {error}")
