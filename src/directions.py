# Controller for directions
# Marcus Kok 1/16/22
import json, html, requests
import os
from dotenv import load_dotenv
from pathlib import Path
from bs4 import BeautifulSoup

# set up of env variables
load_dotenv()

api_key = os.getenv('API_KEY')

class DirectionController():
    # FIFO instruction queue
    instruction_queue = []

    def __init__(self, pointA, pointB):
        self.user_origin = pointA
        self.user_destination = pointB

    # Handler function to retrieve directions from Google api
    def getDirections(self):
        url = 'https://maps.googleapis.com/maps/api/directions/json'
        # define parameters for http request
        params = dict(
            origin = self.user_origin,
            destination = self.user_destination,
            key = api_key
        )

        resp = requests.get(url = url, params = params)
        directions = json.loads(resp.text)
        # print(directions)
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
                    self.instruction_queue.append(instruction)
        
        return directions

    def getInstructions(self):
        return self.instruction_queue

        