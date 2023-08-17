import json
from pprint import pprint
def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
   
    filename=json.dumps(randomuser_data)
    return filename
f=open('randomuser_data.json','r')
randomuser_data=f.read()
pprint(get_data(f))