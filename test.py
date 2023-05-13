from app import app

def test1():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test2():
    response = app.test_client().get('/dbbase')
    assert response.status_code == 200

def test3():
    response = app.test_client().get('/')
    assert b'Welcome to my Flask Login Page !!' in response.data

