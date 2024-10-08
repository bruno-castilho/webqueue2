from lib import app


@app.get("/app")
async def root():
    return {"message": "Hello!"}
