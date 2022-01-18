# Controller for directions
# Marcus Kok 1/16/22
import json, html, requests
import os
from dotenv import load_dotenv
from pathlib import Path
from bs4 import BeautifulSoup

# set up of env variables
dotenv_path = Path('../pathfinder/.env') 
load_dotenv(dotenv_path=dotenv_path)
api_key = os.getenv('API_KEY')

# FIFO instruction queue
instruction_queue = []

class directionController():
    def sayHello():
        return "Hello from directions.py!"

    # Handler function to retrieve directions from Google api
    def getDirections(user_origin, user_destination):
        url = 'https://maps.googleapis.com/maps/api/directions/json'
        # define parameters for http request
        params = dict(
            origin = user_origin,
            destination = user_destination,
            key = api_key
        )

        resp = requests.get(url = url, params = params)
        directions = json.loads(resp.text)
        routes = directions['routes']

        # Parse json data looking for instructions and maneuvers
        for route in routes:
            legs = route['legs']
            for leg in legs:
                steps = leg['steps']
                for step in steps:
                    # instructions from json are in html format
                    # parsing using BeautifulSoup is required for text
                    ins_html = BeautifulSoup(step['html_instructions'], 'html.parser') 
                    instruction = ins_html.get_text()
                    instruction_queue.append(instruction)
        
        return 

    def getInstructions():
        return instruction_queue

        