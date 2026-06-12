from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, Mundo!'}


def test_root_html_retornar_ok(client):

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'].startswith('text/html')
    assert '<h1> Olá, Mundo!</h1>' in response.text


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'fulano',
            'password': 'senha',
            'email': 'fulano@gmail.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'email': 'fulano@gmail.com',
        'username': 'fulano',
        'id': 1,
    }


def test_read_users(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'email': 'fulano@gmail.com',
                'username': 'fulano',
                'id': 1,
            }
        ]
    }


def test_update_existent_userId(client):

    response = client.put(
        '/users/1',
        json={
            'username': 'ciclano',
            'email': 'ciclano@gmail.com',
            'password': 'test',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'ciclano',
        'email': 'ciclano@gmail.com',
        'id': 1,
    }


def test_update_Nonexistent_userId(client):

    response = client.put(
        '/users/2',
        json={
            'username': 'Gades',
            'email': 'gades@gmail.com',
            'password': 'test',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_existent_user(client):

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_Nonexistent_user(client):

    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
