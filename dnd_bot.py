import requests
import json
import random
import lightbulb
import os
import re

from dotenv import load_dotenv
load_dotenv()
  
        

class Dnd_Bot:
    
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
        """Accepts JSON data and constructs a URL."""
        
        api_url_base = "https://www.dnd5eapi.co"
        self.url =  api_url_base + self.url_endpoint
        return
        
    def fact_request(self, url=None):
        """
        Sends a request to dnd5eapi and returns a D&D fact.
        """
        try:
            r: dict = requests.get(self.url)
            self.fact = r.json()
            if len(self.fact["desc"][0]) > 1900:
                self.fact_request()
            return
        except requests.ConnectionError as e:
            print("Network error, can not connect to dnd5eapi.co",e)
            
        
    def __str__(self):
        """
        Returns name and description
        """
        desc = re.sub(r'[\[\]]', r'', str(self.fact["desc"]))
        response = "DND Fact ----> {} , {}".format(self.fact["name"], desc)
        if len(response) > 2000:
            response = response[:2000] + "..."
        return response
    
    def bot_run(self):
        
        TOKEN = os.getenv("DISCORD_TOKEN")
        bot = lightbulb.BotApp(token=TOKEN, )
        
        # Add a /help command
        @bot.command
        @lightbulb.command("help", "description")
        @lightbulb.implements(lightbulb.SlashCommand)
        async def help_command(ctx):
            # Return a message with instructions on how to use the bot
            await ctx.respond("To get a random D&D fact, use the `/fact` command.")
        
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
