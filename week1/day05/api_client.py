import requests

payload = {
    "prompt": "Explain Python loops",
    "risk_level": "low"
}

response = requests.post(
    "https://httpbin.org/post",
    json=payload
)

print(response.status_code)
print(response.json())
