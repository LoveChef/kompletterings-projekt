import requests

class TMDb:
    def __init__(self, api_key):
        self.base_url = "https://api.themoviedb.org/3"
        self.api_key = api_key

    def search_movie(self, query):
        url = f"{self.base_url}/search/movie"
        params = {"api_key": self.api_key, "query": query}
        response = requests.get(url, params=params)
        data = response.json()
        return data["results"]

    def search_tv_show(self, query):
        url = f"{self.base_url}/search/tv"
        params = {"api_key": self.api_key, "query": query}
        response = requests.get(url, params=params)
        data = response.json()
        return data["results"]

    def search_person(self, query):
        url = f"{self.base_url}/search/person"
        params = {"api_key": self.api_key, "query": query}
        response = requests.get(url, params=params)
        data = response.json()
        return data["results"]

class Media:
    def __init__(self, title, release_date, overview, vote_average):
        self.title = title
        self.release_date = release_date
        self.overview = overview
        self.vote_average = vote_average

    def display_info(self):
        print("Title:", self.title)
        print("Release Date:", self.release_date)
        print("Overview:", self.overview)
        print("Vote Average:", self.vote_average)

class Movie(Media):
    def __init__(self, title, release_date, overview, vote_average):
        super().__init__(title, release_date, overview, vote_average)

class TVShow(Media):
    def __init__(self, title, release_date, overview, vote_average):
        super().__init__(title, release_date, overview, vote_average)

class Person:
    def __init__(self, name, known_for, popularity):
        self.name = name
        self.known_for = known_for
        self.popularity = popularity

    def display_info(self):
        print("Name:", self.name)
        print("Known For:", self.known_for)
        print("Popularity:", self.popularity)

def main():
    api_key = "52642a868038e1153406d79c42346aae"
    tmdb = TMDb(api_key)

    while True:
        print("\n1. Search for a movie")
        print("2. Search for a TV show")
        print("3. Search for a person")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter movie title: ")
            results = tmdb.search_movie(query)
            for result in results:
                movie = Movie(result["title"], result["release_date"], result["overview"], result["vote_average"])
                movie.display_info()

        elif choice == "2":
            query = input("Enter TV show title: ")
            results = tmdb.search_tv_show(query)
            for result in results:
                tv_show = TVShow(result["name"], result["first_air_date"], result["overview"], result["vote_average"])
                tv_show.display_info()

        elif choice == "3":
            query = input("Enter person's name: ")
            results = tmdb.search_person(query)
            for result in results:
                person = Person(result["name"], result["known_for"], result["popularity"])
                person.display_info()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
