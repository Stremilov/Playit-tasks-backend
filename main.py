import asyncio
import uvicorn
import logging

from fastapi import FastAPI

from src.api.routers import all_routers

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.getLogger("tasks_logger")

app = FastAPI(root_path="/playit/tasks")


for router in all_routers:
    app.include_router(router)


async def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)


if __name__ == "__main__":
    asyncio.run(main())
