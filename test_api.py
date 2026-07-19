import requests
import pytest

def test_get_user_status_code():
    res = requests.get(" https://jsonplaceholder.typicode.com/users/2")
    body = res.json()
    assert body["id"] == 2
    assert res.status_code == 200
    assert "email" in body
    assert "@" in body["email"]


def test_get_user_response_body():
    response = requests.get("https://jsonplaceholder.typicode.com/users/2")
    data = response.json()
    
    assert data["id"] == 2
    assert "email" in data
    assert "@" in data["email"]

def test_resource_not_found_404_error():
    res = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    assert res.status_code == 404


# POST Request
def test_post_request_201():
    new_user = {
        "name" :"Bharat",
        "Role" : "QA Engineer"
    }
    res = requests.post("https://jsonplaceholder.typicode.com/users",json = new_user)
    assert res.status_code == 201
    body = res.json()
    assert body["name"] == "Bharat"
    assert body["Role"] == "QA Engineer"

# PUT Requyest - Replace a Resource

def test_update_user_PUT():
    new_user = {
        "Name" : "Bharat Singh",
        "Rola" : "Senior QA Engineer"
    }
    res = requests.put("https://jsonplaceholder.typicode.com/users/2", json=new_user)
    assert res.status_code == 200
    body = res.json()
    assert body["Name"] == "Bharat Singh"
    assert body["Rola"] == "Senior QA Engineer"

# PATCH - update a resource
def test_update_resource_PATCH():
    updated_user = {
        "Rola" : "Hired"
        
    }
    res = requests.patch("https://jsonplaceholder.typicode.com/users/2", json=updated_user)
    assert res.status_code == 200
    body = res.json()
    assert body["Rola"] == "Hired"

def test_delete():
    res = requests.delete("https://jsonplaceholder.typicode.com/users/2")
    assert res.status_code == 200


# Fixtures in API

@pytest.fixture
def baseURL():
    return "https://jsonplaceholder.typicode.com"


def test_API(baseURL):
    res = requests.get(f"{baseURL}/users/2")
    body =res.json()
    assert res.status_code == 200

@pytest.mark.parametrize("user_id",[1,2,3,4,5,6])


def test_API_for_multiple_user(baseURL,user_id):
    res = requests.get(f"{baseURL}/users/{user_id}")
    assert res.status_code == 200
















