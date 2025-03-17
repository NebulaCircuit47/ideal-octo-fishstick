import requests

def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    return response.text

url = input("🔗 Enter a long URL: ")
short_url = shorten_url(url)
print(f"🔗 Shortened URL: {short_url}")
