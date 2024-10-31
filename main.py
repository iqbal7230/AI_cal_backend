from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculate.route import router as calculator_router
# from constant import SERVER_URL, PORT, ENV
from dotenv import load_dotenv
import os
load_dotenv()

PORT = os.getenv('PORT')
GEMINI_API_KEY = os.getenv("Gemini_api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Server is running"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])


if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=int(PORT), reload='DEV')