from fastapi.testclient import TestClient
from main import app
from mylib.logic import wiki as summary_wiki

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    default = summary_wiki()
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the web interface!",
        "default": default,
    }


def test_read_phrases():
    response = client.get("/phrases/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }
