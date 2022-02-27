# Controller for directions
# Marcus Kok 1/16/22
""" 
Directions Module
-----------------

This is a module handles all the direction requests and data acquisition for driving instructions.
Uses the Google Places API to gather instruction data.

Attributes
----------
    Typical usage example:

    dirC = new DirectionController("pointA", "pointB")
    dirC.getDirections()
"""
import json, html, requests
import os
from dotenv import load_dotenv
from pathlib import Path
from bs4 import BeautifulSoup

# set up of env variables
load_dotenv()
api_key = os.getenv('API_KEY')

class DirectionController():
    """ Base class for the Direction Controller.
    
    Defines the methods to fetch and store directions using Google Places API.

    Attributes
    ----------
    user_origin:
        Starting origin point defined by user.
    user_destination:
        Final desitnation point defined by user.
    instruction_queue:
        List of instructions obtained from API given source and destination.

    Notes
    -----
    It is critically important that you call getDirections() method first
    before getInstructions() when using this class. The getDirections() method
    fills the instruction_queue which can then be returned by getInstructions().
    Otherwise you will be returning an empty list.
    """
    # FIFO instruction queue
    
    instruction_queue = []

    def __init__(self, pointA, pointB):
        self.user_origin = pointA
        self.user_destination = pointB

    def getDirections(self):
        """ Makes an HTTP request to the Google API endpoint and parses through
        the JSON response to obtain a list of instructions.

        Returns:
            string: Text output of json response.
        """
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
        """ Returns directions.instruction_queue (should be called after .getDirections()).

        Returns: 
            list: list of all instructions 
        """
        return self.instruction_queue
    
    def getManeuvers(self):
        """ Returns list of maneuvers parsed from JSON response after calling .getDirections().

        Returns:
            list: list of all maneuvers
        """
        # not used yet
        return self.maneuver_queue

        