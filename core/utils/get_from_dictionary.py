def get_params_from_dict(element: dict):
    """Get user id and name from [{}]"""
    # Get params 
    user_name = element.get('username')
    user_id = element.get('id')
    return user_name, user_id
