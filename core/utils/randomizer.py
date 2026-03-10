import random 

def get_random_user(users_list: list) -> str:
    """ Get one random user from the list """
    random_user = random.choice(users_list)
    return random_user

# users = ['a', 'b', 'c']

# rand_us = get_random_user(users)
# print(rand_us)