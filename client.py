import aiohttp
import asyncio
import json

async def make_request():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://localhost:8000/essay/invoke",
            json={'input': {'topic': "My best friend"}}
        ) as response:
            content_type = response.headers.get('content-type')
            if content_type == 'application/json':
                json_response = await response.json()
                print(json_response)
            elif content_type == 'text/plain; charset=utf-8':
                # Handle the case where the server responds with plain text
                plain_text_response = await response.text()
                print("Received plain text response:", plain_text_response)
            else:
                print("Received unexpected content type:", content_type)

# Run the asynchronous function
asyncio.run(make_request())