# Pathfinder 
Code for fetching and displaying directions and obd2 metrics <br />

## [PathFinder documentation](https://marcusk19.github.io/PathFinder/pathfinder.html#submodules "read the docs") ## 

---------------

## Structure ##
Breakdown of file structure: <br />
* **docs** - contains documentation for codebase
* **docsrc** - for using sphinx to autogenerate docs
* **src** - most important directory, contains code for PathFinder
* **tests** - contains code for testing *(no longer in use)*


## Getting Started ##

Download this repo by running `git clone https://github.com/Marcusk19/Pathfinder.git`
or alternatively download from GitHub as zipfile and unpack it.

Main code for HUD and directions can be found in *src* 

To run code first enter working directory:
`cd pathfinder` <br />
Install dependencies with:
`pip install -r requirements.txt` <br />
or... <br />
`make init` <br />
Then execute binary:
`make run` <br />
Navigate to [*http://pfnder.ddns.net*](http://pfnder.ddns.net) <br />
![website](readme_images/website.png "pfnder.ddns.net")
From there you can enter a source and destination <br />
Go back to console and observe output: <br />
![output](readme_images/terminal_output.png "terminal output")

## Running in a container ##
*NOTE: this information is deprecated as it was written at initialization of the project.* <br />
Due to differences in local environments, it may be necessary to run the code in a container <br />
In order to do so you must have docker installed on your machine - follow the instructions [here](https://www.docker.com/get-started) to get started <br />
Download the Docker Desktop and build the image by running: `docker build -t pathfinder .` <br />
Check that the image has been created: `docker images` <br />
Run the program by using: `docker run -it pathfinder python3 src/HUD.py` <br />
Changes in code can be pushed to the container through: `docker build -t pathfinder:latest .` <br />

## Setting up your API key ##
Follow this guide [here](https://developers.google.com/maps/documentation/directions/quickstart "Google Directions") to get setup with a Google developer account and obtain your api key.<br />
View the `example.env` file to see how you should set up your .env file and replace `my_api_key` with the api key you received from Google. <br /> 

## Messaging System ##
Code uses MQTT messaging protocol to send and receive information. Depicted below is the flow of data for the PathFinder: <br />
![diagram](readme_images/mqtt.jpg "information flow") <br />
Code for our client can be found [here](https://github.com/Marcusk19/MQTT-web-app "webapp")

## Writing the docs ##
Change working directory to docsrc `cd docsrc` <br />
Run `make github` - html documentation can be found in docs directory. <br />

[TODO]
## External Links ##
* [Source code for pfnder.ddns.net](https://github.com/Marcusk19/MQTT-web-app "webapp")
* [PathFinder documentation](https://marcusk19.github.io/PathFinder/pathfinder.html#submodules "read the docs")
* [Docker](https://docs.docker.com/get-started/ "Getting started")
* [Git contributing](http://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#Commit-Guidelines "Using git")
* [Python structuring](https://docs.python-guide.org/writing/structure/ "How to structure python code")
* [Python testing](https://docs.python-guide.org/writing/tests/ "How to test your code")
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/ "BeautifulSoup Documentation")
* [OBD.py](https://python-obd.readthedocs.io/en/latest/ "OBD python library")

