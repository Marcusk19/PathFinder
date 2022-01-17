# Controller for directions
# Marcus Kok 1/16/22
import json, html, requests
import os
from dotenv import load_dotenv
from pathlib import Path

# set up of env variables
dotenv_path = Path('../pathfinder/production.env') 
load_dotenv(dotenv_path=dotenv_path)
api_key = os.getenv('API_KEY')

# instruction queue
instruction_queue = []

class directionController():
    def sayHello():
        return "Hello from directions.py!"

    def getNextDir():
        nextDir = "NULL"
        return nextDir

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
                    instruction = step['html_instructions']
                    instruction_queue.append(html.unescape(instruction))
        
        return 

    def getInstructions():
        return instruction_queue

        