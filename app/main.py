from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(
    title="DevOps Automation API",
    description="A simple API built for learning automation and DevOps concepts.",
)

# Endpoint 1: Root endpoint (welcome page)
@app.get("/")
def read_root():
  # Logging execution to console
  print("GET request received at '/' endpoint.")
  return {"status": "API works!", "goal": "DevOps Automation"}


# Endpoint 2: Health check endpoint (useful for monitoring/Kubernetes probes)
@app.get("/health")
def health_check():
  print("GET request received at '/health' endpoint.")
  return {"status": "ok", "cpu_load": "normal", "memory": "available"}


# Endpoint 3: Personalized greeting endpoint with path parameter
@app.get("/hello/{name}")
def say_hello(name: str):
  print(f"GET request received at '/hello/{name}' endpoint.")
  return {"message": f"Hello, {name}! Welcome to automation."}


# Startup message when running the file directly
if __name__ == "__main__":
  print("Application setup complete. Run via Uvicorn to start the server.")