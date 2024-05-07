import requests

class API:
    def __init__(self, api_key):
        self.api_key = api_key
        api_key = "52642a868038e1153406d79c42346aae"

    def apidata(self, search):
        url = f"https://api.themoviedb.org/3/search/{type}?api_key={self.api_key}&query={search}"
        response = requests.get(url)
        data = response.json()