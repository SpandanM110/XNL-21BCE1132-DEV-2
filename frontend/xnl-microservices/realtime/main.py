import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

start_server = websockets.serve(handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
