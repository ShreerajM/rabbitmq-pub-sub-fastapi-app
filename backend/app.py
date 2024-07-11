import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from routes.status import status_router
from messaging import close_channel
from messaging.consumer import start_consumer, stop_consumer
from messaging.publisher import start_publisher, stop_publisher
import threading


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    consumer_thread = threading.Thread(target=start_consumer)
    consumer_thread.start()
    publisher_thread = threading.Thread(target=start_publisher)
    publisher_thread.start()

    yield
    # Shutdown event
    stop_publisher()
    stop_consumer()



app = FastAPI(lifespan=lifespan)

app.include_router(status_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
