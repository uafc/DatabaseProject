To run this program:
- First ensure that you have virtualenv installed: https://virtualenv.pypa.io/en/latest/installation.html#via-pip
- Then, create a virtual environment by typing into your terminal: virtualenv -p python3 .venv
- Then, activate your virtual environment by doing: source .venv/bin/activate
- Once you have activated your virtual environment, type into your terminal: pip install -r requirements.txt. This will install the required python packages inside of your virtual environment
- Once you have finished working in your virtual environment, type "deactivate" in terminal to deactivate your virtual environment.

- Once you have cloned the repo, in your local repo folder, create a .env file. This file will be used to store your OMDB API Key, which the python program will extract and use.
- In your .env file, write the following line: OMBD_API_KEY = api_key (where api_key is your actual api_key, with no quotation marks)  
