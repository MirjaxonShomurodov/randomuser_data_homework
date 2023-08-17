import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
data= {
        1:"1_krs",
        2:"2_krs",
        3:"3_krs",
        4:"4_krs"
    }
for i in data:
        print(i+1)
print(get_count_users(data))
    
