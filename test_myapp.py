from app import app, multiply


def test_home_route():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Stephens application"


def test_multiply_function():
    result = multiply()
    assert result == 12
