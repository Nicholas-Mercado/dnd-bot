import requests
import json
import random
    
class Dnd_Bot:
    # TODO: Clean up output data
    def __init__(self, url_endpoint=None, data=None, url="", fact=None):
        self.fact: dict = fact
        self.url: str = url
        self.data: dict = data
        self.url_endpoint: str = url_endpoint
        
    
    def retrieve_url(self):
        """
        Reads json file containing url endpoints 
        """
        with open('url_builder_data.json') as f:
            self.data = json.load(f)
        return
    
    def random_url_data(self):
        """
        Randomly chooses and returns url endpoint
        """
        random_number = random.randint(1, 417)
        self.url_endpoint = self.data['results'][random_number]['url']
        return    
        
        
    def url_builder(self):
        """
        Takes in json data and builds url
        """
        api_url_base = "https://www.dnd5eapi.co"
        self.url =  api_url_base + self.url_endpoint
        return
        
    def fact_request(self, url=None):
        """
        Hits dnd5eapi and returns Dnd fact
        """
        r: dict = requests.get(self.url)
        self.fact = r.json()
        return
    
    def __str__(self):
        """
        Returns name and description
        """
        return self.fact["name"], self.fact["desc"]

if __name__ == '__main__':
    fact1 = Dnd_Bot()
    fact1.retrieve_url()
    fact1.random_url_data()
    fact1.url_builder()
    fact1.fact_request()
    print(fact1.url)
    print(fact1.__str__())
