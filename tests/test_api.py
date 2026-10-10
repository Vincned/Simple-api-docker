from fastapi.testclient import TestClient
from app.main import app

# Base URL of our local API
client = TestClient(app)


def test_home_endpoint():
  print("Testing root endpoint '/'...")
  response = client.get("/")

  # Assert status code is 200 OK
  assert (
      response.status_code == 200
  ), f"Expected status 200, got {response.status_code}"

  # Check JSON response content
  data = response.json()
  assert data["status"] == "API works!"
  print("Root endpoint test passed successfully!\n")


def test_health_endpoint():
  print("Testing health check endpoint '/health'...")
  response = client.get(f"/health")

  assert response.status_code == 200
  data = response.json()
  assert data["status"] == "ok"
  print(f"Health check passed. Current system status: {data['status']}\n")


def test_hello_endpoint():
  name = "DevOpsEngineer"
  print(f"Testing personalized endpoint '/hello/{name}'...")
  response = client.get(f"/hello/{name}")

  assert response.status_code == 200
  data = response.json()
  assert name in data["message"]
  print(f"Received message: '{data['message']}'")
  print("Hello endpoint test passed successfully!\n")


if __name__ == "__main__":
  print("=== Starting API Automation Tests ===\n")
  try:
    test_home_endpoint()
    test_health_endpoint()
    test_hello_endpoint()
    print("=== All automated tests passed! ===")
  except AssertionError as e:
    print(f"Test FAILED: {e}")
  except client.exceptions.ConnectionError:
    print("Test FAILED: Could not connect to the API. Is the Uvicorn server running?")