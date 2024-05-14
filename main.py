import requests

class TMDBSearch:
    """hanterar sökningen av filmer, tvserier, skådisar med apin

    Returns:
        api_url(str): Bas urlen för apin, man lägger till efter 3 så sorterar den rätt.
    """
    api_url = "https://api.themoviedb.org/3"
    def __init__(self, api_key):
        """Sätter igång tmdbsearch med apinyckeln

        Args:
            api_key (str): api nyckeln
        """
        self.api_key = api_key
    
    def search(self, type, query):
        """¨Söker efter skådisar, filmer o tvserier

        Args:
            type (str): Om det är en skådespelare, film eller tv serie
            query (str): Sökningen

        Returns:
            list: lista på sökningsresultat.
        """
        url = f"{self.api_url}/search/{type}"
        parameter = {"api_key": self.api_key, "query": query}
        response = requests.get(url, parameter=parameter)
        data = response.json()
        
        return data ["results"]
        
        
        
class TMDB:
    """
    Attributes:
      title (str): Titel
      date (str): Publiceringsdatum .
      overview (str): SUmmering.
      vote (float): Betyg.
    """
    def __init__(self, title, date, overview, vote):
        self.title = title
        self.date = date
        self.overview = overview
        self.vote = vote
        
    def show_info(self):
        """Printar informationmen
        """
        print("- - - - - - - - - - ")
        print("📜|Title:", self.title)
        print("📆|Date:", self.date)
        print("📝|Overview:", self.overview)
        print("⭐|Votes:", self.vote)
        print("- - - - - - - - - - ")
    
    def show_result(api, type, query, tmdb_class):
        result = api.search(type, query)
        for result in result:
            tmdb = tmdb_class(result["title"], result.get("release_date"), result["overview"], result["vote_average"])
            tmdb.show_info()