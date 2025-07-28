from fastapi import FastAPI
from users.routers import user_router
from auth.routers import auth_router
from posts.routers import post_router
from base.database import _db_init
import uvicorn
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await _db_init()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/users")
app.include_router(auth_router, prefix="/auth")
app.include_router(post_router, prefix="/posts")


@app.get("/")
async def root():
    return {"message": "API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

