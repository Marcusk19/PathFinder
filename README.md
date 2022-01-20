Pathfinder
========================

Structure of this codebase follows best practices recommendations
`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.

## Structure ##
Breakdown of file structure: <br />
* **docs** - contains documentation (not used yet)
* **sample** - contains sample code from GitHub used for structuring this repo
* **src** - most important directory, contains code for PathFinder
* **target** - not sure what this one is for yet
* **tests** - contains code for testing

## Getting Started ##

Download this repo by running `git clone https://github.com/Marcusk19/Pathfinder.git`
or alternatively download from GitHub as zipfile and unpack it.

Main code for HUD and directions can be found in *src* 

To run code first enter working directory:
`cd pathfinder` <br />
Install dependencies with:
`pip install -r requirements.txt` <br />
Then execute binary:
`python src/HUD.py "ORIGIN" "DESTINATION"` <br />

## Running in a container ##

Due to differences in local environments, it may be necessary to run the code in a container <br />
In order to do so you must have docker installed on your machine - follow the instructions [here](https://www.docker.com/get-started) to get started <br />
Download the Docker Desktop and build the image by running: `docker build -t pathfinder .` <br />
Check that the image has been created: `docker images` <br />
Run the program by using: `docker run -it pathfinder python3 src/HUD.py 'POINT_A' 'POINT_B'` <br />
Changes in code can be pushed to the container through: `docker build -t pathfinder:latest .` <br />

## Setting up your API key ##
Follow this guide [here](https://developers.google.com/maps/documentation/directions/quickstart "Google Directions") to get setup with a Google developer account and obtain your api key.<br />
View the `example.env` file to see how you should set up your .env file and replace `my_api_key` with the api key you received from Google. <br /> 

[TODO]
## External Docs ##
* [Tkinter](https://docs.python.org/3/library/tkinter.html "Tkinter docs")
* [Git contributing](http://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#Commit-Guidelines "Using git")
* [Python structuring](https://docs.python-guide.org/writing/structure/ "How to structure python code")
* [Python testing](https://docs.python-guide.org/writing/tests/ "How to test your code")
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/ "BeautifulSoup Documentation")
