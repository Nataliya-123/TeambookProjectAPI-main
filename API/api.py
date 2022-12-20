import requests
import json
import uuid

email = uuid.uuid4().hex
name = (str(uuid.uuid4().hex))


class Teambook:
    def __init__(self):
        self.base_url = 'https://web.teambooktest.com/api/'

    def login(self) -> json:
        '''Авторизация пользователя'''

        params = {
            "user[email]": 'teambooktest@gmail.com',
            "user[password]": 'teambooktest1'
        }
        res = requests.post(self.base_url + 'auth/login',
                            data=params)
        print(res.text.split('"'))
        token = (res.text.split('"')[1])
        print(res.content)
        print(token)
        return token

    def get_user(self) -> json:
        '''Получение списка пользователей'''
        data = {'token': self.login()}
        print(data)
        res = requests.get(self.base_url + 'users?' + 'data', params=data)
        print(res.content)
        status = res.status_code
        print(status)
        return status

    def create_user(self) -> json:
        '''Создание нового пользователя'''
        my_token = Teambook.login(self)
        data = {'token': f'{my_token}', 'first_name': f'{name}', 'last_name': 'kjk', 'email': f'{email}@uy.lk',
                'role': 'regular', 'billable': 'true', 'tags': ''}
        res = requests.post(self.base_url + 'users', data=data)
        print(res.content)
        print(res.text.split('"'))
        id = (res.text.split('"')[2])
        my_id = (id[1:5])
        print(my_id)
        return my_id

    # def re_invite_user(self) -> json:
    #     '''Отправка повторного приглашения на почту.'''
    #     data = {'token': self.login()}
    #     my_id = Users.create_user(self)
    #     res = requests.post(self.base_url + f'user/{my_id}/reinvite', data=data)
    #     print(res.content)
    #     print(res.text.split('"'))
    #     value = (res.text.split('"')[2])
    #     print(value)
    #     my_value = (value[1:5])
    #     print(my_value)
    #     status = res.status_code
    #     print(status)
    #     return status

    def get_user_exists(self) -> json:
        '''Убедиться, что юзер сущетсвует по элетронной почте.'''

        data = {'email': f'{email}@uy.lk'}
        res = requests.get(self.base_url + 'users/exists', data=data)
        print(res.content)
        status = res.status_code
        print(status)
        return status

    # def deactivate_user(self) -> json:
    #     '''Деактивация юзера. не понятно, как заполнить  id'''
    #     my_token = Users.login(self)
    #     my_id = Users.create_user(self)
    #     data = {'token': f'{my_token}', 'user_ids':f'{my_id}'}
    #     res = requests.patch(self.base_url + 'user/deactivate' , data=data)
    #     print(res.content)

    def get_user_deactivate(self) -> json:
        '''Получить список деактивированных юзеров'''
        my_token = Teambook.login(self)
        data = {'token': f'{my_token}'}
        res = requests.get(self.base_url + 'users/deactivated?' + 'data', data=data)
        print(res.content)
        status = res.status_code
        print(status)
        return status


Teambook().login()
Teambook().get_user()
# Users().re_invite_user()
# Users().deactivate_user()
Teambook().get_user_exists()
Teambook().create_user()
Teambook().get_user_deactivate()
