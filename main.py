import requests

class API:
    def __init__(self, api_key):
        """Skapar instans av api klassen

        Args:
            api_key (str): api nyckeln för tmdb
        """
        self.api_key = api_key

    def apidata(self, search, type):
        """Hämtar datan från api:n

        Args:
            search (str): sökningen på film, tv serie osv
            type (str): typen av sökning, alltså om du vill söka på en film eller tv serie

        Returns:
            _type_: _description_
        """
        
        url = f"https://api.themoviedb.org/3/search/{type}?api_key={self.api_key}&query={search}"
        response = requests.get(url)
        data = response.json()
        
        result = []
        for item in data["results"]:
            if type == "movie":
                result.append(Movie(self.api_key, item["title"], search))
        return result

class Movie:
    def __init__(self, api_key, title, search):
        """sklapar instans av movie klassen

        Args:
            api_key (str): api nyckeln
            title (str): filmens titel
        """
        self.api_key = api_key
        self.titel = title
        self.search = search

    def movie_info(self):
        """Hämtar information om filmen från api
        """
        url = f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={self.search}"
        response = requests.get(url)
        data = response.json()

        print(f"Info om: {self.titel}")
        print(f"Beskrivning: {data['overview']}")
        print(f"Betyg: {data['vote_average']}")

def meny():
    print("Välj alternativ")
    print("1. Film")
    choice = input("Skriv in ditt val: ")
    if choice == '1':
        search = input("Skriv namnet på filmen: ")
        movies = api.apidata(search, "movie")
        for movie in movies[:1]:
            movie.movie_info()
            
api_key = "52642a868038e1153406d79c42346aae" # Måste ha nyckeln här nu istället, enda stället det funkar på 
api = API(api_key)
meny()