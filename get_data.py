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
   
    f=json.loads(data)
    return f
f=open('randomuser_data.json','r')
data=f.read()
pprint(get_data(f))