from fastapi import FastAPI
from routers import load_data

app = FastAPI()
app.include_router(load_data.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=9000)