from fastapi import FastAPI, Request, Response

app = FastAPI()
@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    print("Before request")
    response: Response = await call_next(request)
    response.headers["X-Custom-Header"] = "Custom Value"
    print("After request")
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}