import os
os.environ["DATABASE_URL"]="sqlite:///./test_pocketsmart.db"
os.environ["SECRET_KEY"]="test-secret"
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def auth():
    email="testuser@example.com"
    client.post("/api/register",json={"name":"Test User","email":email,"password":"secret123"})
    r=client.post("/api/login",json={"email":email,"password":"secret123"})
    return {"Authorization":"Bearer "+r.json()["access_token"]}

def test_health():
    assert client.get("/health").json()["status"]=="ok"

def test_session():
    r=client.get("/api/session-info",headers=auth()); assert r.status_code==200

def test_home():
    r=client.post("/api/generate-home",headers=auth(),data={"budget":50000,"rooms":"Living Room,Bedroom","style":"Modern","notes":""})
    assert r.status_code==200 and r.json()["planner"]=="home"

def test_party():
    r=client.post("/api/generate-party",headers=auth(),data={"budget":25000,"guests":20,"event_type":"Birthday","venue":"Home","notes":""})
    assert r.status_code==200 and r.json()["planner"]=="party"

def test_jewelry():
    r=client.post("/api/generate-jewelry",headers=auth(),data={"budget":5000,"occasion":"Wedding","style":"Elegant","metal":"Gold-tone","notes":""})
    assert r.status_code==200 and r.json()["planner"]=="jewelry"
