from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users', json={  # некоректный запрос, такой id уже существует
    'id': 1,
    'name': "Эмильджан",
    'about': "О ком-то",
    'email': 'ha4-pay@mail.ru',
    'hashed_password': '12341234'}).json())
print(post('http://localhost:5000/api/v2/users', json={  # коректный запрос
    'id': 6,
    'name': "Эмильджан",
    'about': "О ком-то",
    'email': 'ha4-pay@mail.ru',
    'hashed_password': '12341234'}).json())
print(post('http://localhost:5000/api/v2/users', json={  # некоректный запрос
    'about': "О ком-то",
    'email': 'ha4-pay@mail.ru',
    'hashed_password': '12341234'}).json())
print(get('http://localhost:5000/api/v2/users').json())
print(delete('http://localhost:5000/api/v2/users/5').json())
print(get('http://localhost:5000/api/v2/users').json())

