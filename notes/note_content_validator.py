import re
import httpx
from config import YANDEX_SPELLER_API_URL


async def validate_content(content: str) -> str:
    async with httpx.AsyncClient() as client:
        payload = {"text": content}
        response = await client.post(YANDEX_SPELLER_API_URL, data=payload)
        for typo in response.json():
            content = re.sub(rf'\b{typo['word']}\b', typo['s'][0], content)
        return content
