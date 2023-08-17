import json
from pprint   import pprint

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    resulte = data.get('results')
    users_gender=[]
    for user in resulte:
        users_gender.append(user['gender'])
    return users_gender

f=open('randomuser_data.json','r')
data=json.loads(f.read())

pprint(get_gender_users(data))
