from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_jobs():
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
