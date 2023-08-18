import json
from pprint import pprint
def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    r = data.get('results')
    g=[]
    for user in r:
        name = user['name']
        first = name['first']
                
        u= {
            "first":first
            
        } 
        g.append(u)

    return g

f=open('randomuser_data.json','r')
data=json.loads(f.read())
pprint(get_count_users(data))