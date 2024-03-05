from rest_framework.test import RequestsClient
import unittest
import json

base_url = "http://127.0.0.1:8000/api/"

test_user_data = {
  "first_name": "Max",
  "last_name": "Mustermann",
  "birthday": "1990-12-31",
  "street": "Musterstraße",
  "house_number": "12a",
  "postcode": 10365,
  "city": "Berlin-Lichtenberg",
}

class TestBackend(unittest.TestCase):
  def get_token(self):
    client = RequestsClient()
    token_post_response = client.post(f"{base_url}login", { "username": "admin", "password": "rootpw123" })
    token_post_response_content = json.loads(token_post_response.content)
    return token_post_response_content["token"]
  
  def test_member_endpoint(self):
    client = RequestsClient()
    client.headers.update({"Authorization": f"Token {self.get_token()}", "Content-Type": "application/json"})
    
    #Post a new member
    member_post_response = client.post(f"{base_url}member", data=json.dumps(test_user_data))
    assert member_post_response.status_code == 201
    
    #Save the id
    member_id = json.loads(member_post_response.content)["data"]["id"]
    
    #Get the new member
    member_get_response = client.get(f"{base_url}member?id={member_id}")
    member_get_response_content = json.loads(member_get_response.content)
    assert member_get_response_content["data"][0]["first_name"] == test_user_data["first_name"]
    assert member_get_response_content["data"][0]["last_name"] == test_user_data["last_name"]
    assert member_get_response_content["data"][0]["street"] == test_user_data["street"]
    assert member_get_response_content["data"][0]["house_number"] == test_user_data["house_number"]
    assert member_get_response_content["data"][0]["birthday"] == test_user_data["birthday"]
    assert member_get_response_content["data"][0]["postcode"]["postcode"] == test_user_data["postcode"]
    assert member_get_response_content["data"][0]["postcode"]["city"] == test_user_data["city"]
 
    #Put a update to new member
    member_put_response = client.put(f"{base_url}member", data=json.dumps({"id": member_id, **test_user_data, "postcode": {"postcode": test_user_data["postcode"], "city": test_user_data["city"]}, "house_number": "82b"}))
    member_put_response_content = json.loads(member_put_response.content)
    assert member_put_response.status_code == 200
    assert member_put_response_content["data"]["house_number"] == "82b"
    
    #Delete the new member / to not effect db
    member_delete_response = client.delete(f"{base_url}member?id={member_id}")
    assert member_delete_response.status_code == 204
  