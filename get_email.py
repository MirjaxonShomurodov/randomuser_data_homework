import json
from pprint import pprint
def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    result= data.get('results')
    user_email=[]
    
    for user in result:
        email = user['email']

        user_data = {
            "email_number":email
        }

        user_email.append(user_data)

    return user_email 

f = open('randomuser_data.json','r')

data=json.loads(f.read())

pprint(get_email(data))

