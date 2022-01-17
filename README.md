Pathfinder
========================

Structure of this codebase follows best practices recommendations
`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.

## Getting Started ##

Download this repo by running `git clone https://github.com/Marcusk19/Pathfinder.git`
or alternatively download from GitHub as zipfile and unpack it.

Main code for HUD and directions can be found in *src* 

To run code first enter working directory:
`cd pathfinder` <br />
Install dependencies with:
`pip install -r requirements.txt` <br />
Then execute binary:
`python3 src/HUD.py` <br />

TODO

## Setting up your API key ##
Follow this guide [here](https://developers.google.com/maps/documentation/directions/quickstart "Google Directions") to get setup with a Google developer account and obtain your api key.<br />
View the `example.env` file to see how you should set up your .env file and replace `my_api_key` with the api key you received from Google. <br /> 


## External Docs ##
* [Tkinter](https://docs.python.org/3/library/tkinter.html "Tkinter docs")
* [Git contributing](http://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#Commit-Guidelines "Using git")
* [Python structuring](https://docs.python-guide.org/writing/structure/ "How to structure python code")
* [Python testing](https://docs.python-guide.org/writing/tests/ "How to test your code")
