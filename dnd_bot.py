import requests
    
class Dnd_Bot:
    
    def __init__(self, fact=None):
        self.fact = fact
        
    def fact_request(self):
        """
        Hits dnd5eapi and returns Dnd fact
        """
        r = requests.get("https://www.dnd5eapi.co/api/ability-scores/str")
        self.fact = r.json()
        print(self.fact)
        return
    
    def __str__(self):
        """
        Returns name and description
        """
        return self.fact["full_name"], self.fact["desc"]

if __name__ == '__main__':
    fact1 =Dnd_Bot()
    fact1.fact_request()
    print(fact1.__str__())
