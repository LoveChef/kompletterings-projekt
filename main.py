import requests

class API:
    def __init__(self, api_key):
        self.api_key = api_key
        api_key = "52642a868038e1153406d79c42346aae"

    def apidata(self, search, type):
        url = f"https://api.themoviedb.org/3/search/{type}?api_key={self.api_key}&query={search}"
        response = requests.get(url)
        data = response.json()
        
        result = []
        for item in data["results"]:
            if type == "movie":
                result.append(Movie(item["title"]))
        return result

class Movie:
    def __init__(self, api_key, title):
        self.api_key = api_key
        self.titel = title

    def movie_info(self):
        url = f"https://api.themoviedb.org/3/movie/?api_key={self.api_key}&query={search}"
        response = requests.get(url)
        data = response.json()

        print(f"Info om: {self.titel}")
        print(f"Beskrivning: {data['overview']}")
        print(f"Betyg: {data['vote_average']}")

def meny(result, type):
    print("Välj alternativ")
    for i, item in enumerate