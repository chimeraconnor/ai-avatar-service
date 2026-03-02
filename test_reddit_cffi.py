from curl_cffi import requests

response = requests.get(
    "https://old.reddit.com/r/LocalLLaMA/new.json?limit=1",
    impersonate="chrome110",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
)

print(response.status_code)
print(response.text[:500])
