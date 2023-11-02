from fastapi import FastAPI
from routers import update_data_router

app = FastAPI()
app.include_router(update_data_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
