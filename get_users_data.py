import json
from pprint import pprint

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    resulte = data.get('results')
    users_gender=[]
    for user in resulte:
        name = user['name']
        first = name['first']
        last = name['last']
        email = user['email']
        phone = user['phone']
        


        user_data= {
            "first_name":first,
            "last_name":last,
            "email_number":email,
            "phone_number":phone,
            
        } 
        users_gender.append(user_data)

    return users_gender

f=open('randomuser_data.json','r')
data=json.loads(f.read())
pprint(get_users_data(data))

# dict_data=get_users_data(data)
# json_data = json.dumps(dict_data ,indent=4)
# w= open('users.json','w')
# w.write(json_data)
# w.close()