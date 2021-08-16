from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ner_endpoint_given_json_body_returns_200():
    response = client.post("/ner", json={"sentence": "地球是太阳系中由内及外的第三颗行星。"})
    assert response.status_code == 200

def test_ner_endpoint_matches_known_entities():
    response = client.post("/ner", json={"sentence": "地球是太阳系中由内及外的第三颗行星。"})
    data = response.json()
    assert data['entities'][0]['ent'] == '地球'
    assert data['entities'][0]['label'] == '地点'