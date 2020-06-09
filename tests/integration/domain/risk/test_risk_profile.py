import json

def test_requests_risk_profile_with_valid_body(client):
    VALID = {
      "age": 35,
      "dependents": 2,
      "house": {"ownership_status": "owned"},
      "income": 0,
      "marital_status": "married",
      "risk_questions": [0, 1, 0],
      "vehicle": {"year": 2018}
    }

    response = client.post(
        '/risk-profile', data=json.dumps(VALID), content_type='application/json'
    )

    assert response.status_code == 201

def test_requests_risk_profile_with_invalid_body(client):
    INVALID = {
      "age": 35,
      "dependents": 2,
      "house": {"ownership_status": "owned"},
      "marital_status": "married",
      "risk_questions": [0, 1, 0],
      "vehicle": {"year": 2018}
    }

    response = client.post(
        '/risk-profile', data=json.dumps(INVALID), content_type='application/json'
    )

    assert response.status_code == 400

def test_requests_risk_profile_with_wrong_values(client):
    INVALID = {
      "age": -1231,
      "dependents": 2,
      "house": {"ownership_status": "owned"},
      "marital_status": "married",
      "risk_questions": [0, 1, 0],
      "vehicle": {"year": 2018}
    }

    response = client.post(
        '/risk-profile', data=json.dumps(INVALID), content_type='application/json'
    )

    assert response.status_code == 422
    assert response.json['message'] == 'age must be equals or greater than zero'
