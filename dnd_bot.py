import requests
import json
import random
import lightbulb
import os

from dotenv import load_dotenv
load_dotenv()
  
        

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
        try: 
            with open('url_builder_data.json') as f:
                self.data = json.load(f)
            return
        except FileNotFoundError as e:
            print("Sorry, file not found",e)
        except Exception as e:
            print(e)
    
    def random_url_data(self):
        """
        Randomly chooses and returns url endpoint
        """
        random_number = random.randint(1, 388)
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
        try:
            r: dict = requests.get(self.url)
            self.fact = r.json()
            return
        except requests.ConnectionError as e:
            print("Network error, can not connect to dnd5eapi.co",e)
            
    def __str__(self):
        """
        Returns name and description
        """
        return self.fact["name"], self.fact["desc"]
    
    def bot_run(self):
        
        TOKEN = os.getenv("DISCORD_TOKEN")
        bot = lightbulb.BotApp(token=TOKEN, )
        @bot.command
        @lightbulb.command("fact", "pong")
        @lightbulb.implements(lightbulb.SlashCommand)
        async def ping(ctx):
            self.retrieve_url()
            self.random_url_data()
            self.url_builder()
            self.fact_request()
            await ctx.respond(self.__str__())
        bot.run()

if __name__ == '__main__':
    fact = Dnd_Bot()
    fact.bot_run()
