import requests
import pytest
import jsonschema
from jsonschema import validate

company_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "address": {"type": "string"},
            "zip": {"type": "string"},
            "country": {"type": "string"},
            "employeeCount": {"type": "integer"},
            "industry": {"type": "string"},
            "marketCap": {"type": "integer"},
            "domain": {"type": "string"},
            "logo": {"type": "string", "format": "uri"},
            "ceoName": {"type": "string"}
        },
        "required": ["id", "name", "address", "zip", "country", "employeeCount", "industry", "marketCap", "domain", "logo", "ceoName"],
        "additionalProperties": False
    }
}

@pytest.mark.api
def test_get_companies():
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    response = requests.get(url)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    try:
        response_json = response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")
    
    try:
        validate(instance=response_json, schema=company_schema)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"JSON does not match the expected schema: {e.message}")
    print(response_json)
