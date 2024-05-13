import requests

class MovieSearch:
    api_url = "https://api.themoviedb.org/3"
    def __init__(self, api_key):
        self.api_key = api_key
    
    def search(self, type, query):
        url = f"{self.api_url}/search/{type}"
        parameter = {"api_key": self.api_key, "query": query}
        response = requests.get(url, parameter=parameter)
        data = response.json()
        
        return data ["results"]
        
        
        
    