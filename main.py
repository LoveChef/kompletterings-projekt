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
            
        Lösningen med att använda sig av en bas url där man lägger in apin samt typ av sökning tog jag inspiration av från stack
        """
        url = f"{self.api_url}/search/{type}"
        parameter = {"api_key": self.api_key, "query": query}
        response = requests.get(url, params=parameter)
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
        # Infon för film o tv serier
        if type == "movie" or "tv":
            print("📜| Title:", self.title)
            print("📆| Release Date:", self.date)
            print("📝| Overview:", self.overview)
            print("⭐| Votes:", self.vote)
            print("- - - - - - - - - - ")
        # Infon för film o tv serier
        elif type == "person":
            print("👤| Name:", self.title)
            print("📜| Known for:", self.date)
            print("⭐| Popularity:", self.vote)
            print("- - - - - - - - - - ")
    
def show_result(api, type, query, tmdb_class):
    result = api.search(type, query) # gör sökningen, söker alltså efter parametrarna
    for result in result: # Ifall man väljer t.ex tv så har namnet och datumet andra variabler i apin, den byter alltså ut.
        if type == "movie":
            vote = result["vote_average"]
            overview = result["overview"]
            title= result["title"]
            date = result.get["release_date"]
        elif type == "tv":
            vote = result["vote_average"]
            title = result["name"]
            overview = result["overview"]
            date = result["first_air_date"]
        elif type == "person":
            title = result["name"]
            date = result["known_for_department"]
            vote = result["popularity"]
            overview = ""
        else:
            continue
        
        tmdb = tmdb_class(title, date, overview, vote)        
        tmdb.show_info()

def Main():
    api_key = "52642a868038e1153406d79c42346aae" # Api nyckeln
    tmdb_search = TMDBSearch(api_key) # skapar instansen av tmdbsearchw
    
    while True:
        # menyn
        print("- - - - - - - - - - ")
        print("🍿| 1. Film")
        print("🎥| 2. Tv serie")
        print("👤| 3. Sök efter en skådis")
        print("❌| 4. Stäng")
        print("- - - - - - - - - - ")
        choice = input("🔎|Välj vad du vill söka: ") # valet användaren gör
        
        if choice == "1":
            query = input("🍿| Skriv namnet på filmen: ")
            show_result(tmdb_search, "movie", query, TMDB) # Visar sökresultat för film
        elif choice == "2":
            query = input("🎥| Skriv namnet på TV-serien: ")
            show_result(tmdb_search, "tv", query, TMDB) #-||- serie
        elif choice == "3":
            query = input("👤| Skriv namnet på skådisen: ") #-||- skådis
            show_result(tmdb_search, "person", query, TMDB)
        elif choice == "4": # stänger programmet
            break
        else:
            print("Fel")
if __name__ == "__main__":
    Main()