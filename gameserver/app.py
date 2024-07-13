from pprint import pprint
import uvicorn
import asyncio

async def main():
    config = uvicorn.Config("api:app", port=80, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())