import random


def get_random_user(object_list: list) -> str:
    """Get one random object from the list"""
    random_object = random.choice(object_list)
    return random_object
