import requests
    
class Dnd_Bot:
    
    def __init__(self, fact=None):
        self.fact=fact
        
    def fact_request(self):
        r = requests.get("https://www.dnd5eapi.co/api/ability-scores/str")
        self.fact = r.json
        
    

if __name__ == '__main__':
    fact1 =Dnd_Bot()
    fact1.fact_request()
    print(fact1)
