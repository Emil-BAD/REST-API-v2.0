from requests import get, post, delete

print(get('http://localhost:5000/api/v2/jobs').json())
print(post('http://localhost:5000/api/v2/jobs', json={  # некоректный запрос, такой id уже существует
    'id': 1,
    'name': "Эмильджан",
    'about': "О ком-то",
    'email': 'ha4-pay@mail.ru',
    'hashed_password': '12341234'}).json())
print(post('http://localhost:5000/api/v2/jobs', json={  # коректный запрос
    'id': 11,
    'job': "Делать пельмешки",
    'work_size': 100,
    'collaborators': 3,
    'is_finished': False,
    'team_leader': 1}).json())
print(post('http://localhost:5000/api/v2/jobs', json={  # некоректный запрос
    'about': "О ком-то",
    'email': 'ha4-pay@mail.ru',
    'hashed_password': '12341234'}).json())
print(get('http://localhost:5000/api/v2/jobs').json())
print(delete('http://localhost:5000/api/v2/jobs/11').json())
print(get('http://localhost:5000/api/v2/jobs').json())

