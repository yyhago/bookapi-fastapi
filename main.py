from fastapi import FastAPI
from routes.route import appRouter

app = FastAPI()

app.include_router(appRouter)