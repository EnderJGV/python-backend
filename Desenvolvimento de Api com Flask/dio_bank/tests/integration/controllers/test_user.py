from http import HTTPStatus
from src.app import Role, User, db

def test_get_user_sucess(client):
    # Given
    # Isso faz o insert da role para atribuir ao user
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()

    # Isso faz o insert do user
    user = User(username='john-doe', password='test', role_id=role.id)
    db.session.add(user)
    db.session.commit()

    # When
    # Faz a requisição para o endpoint de get_user e valida se o status code e o retorno estão corretos
    response = client.get(f'/users/{user.id}')

    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "id": user.id,
        "username": user.username,
    }

def test_get_user_not_found(client):
    # Given
    # Isso faz o insert da role para atribuir ao user
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()

    user_id = 1

    # When
    # Faz a requisição para o endpoint de get_user e valida se o status code e o retorno estão corretos
    response = client.get(f'/users/{user_id}')

    # Then
    assert response.status_code == HTTPStatus.NOT_FOUND