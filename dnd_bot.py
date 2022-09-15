import requests
    
class Dnd_Bot:
    # TODO: URL builder Randomizer
    # TODO: Clean up output data
    def __init__(self, url="", fact=None):
        self.fact = fact
        self.url = url
        
    def ability_scores_url_builder(self):
        """
        Builds 
        """
        self.url =  "https://www.dnd5eapi.co/api/skills/arcana"
        return self.url
        
    def fact_request(self, url=None):
        """
        Hits dnd5eapi and returns Dnd fact
        """
        r = requests.get(self.url)
        self.fact = r.json()
        return
    
    def __str__(self):
        """
        Returns name and description
        """
        return self.fact["name"], self.fact["desc"]

if __name__ == '__main__':
    fact1 = Dnd_Bot()
    fact1.ability_scores_url_builder()
    fact1.fact_request()
    print(fact1.__str__())
