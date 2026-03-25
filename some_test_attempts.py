users_list = [{'id': 987603602, 'name': 'Alina Davydenko 💖🫧', 'username': 'Alina_Davydenko7'}, {'id': 156330505, 'name': 'Димка ❤️', 'username': 'dmitrymp3'}]

for element in users_list:
    user_name = element.get('username')
    user_id = element.get('id')

    print(f'{user_name} : {user_id}')