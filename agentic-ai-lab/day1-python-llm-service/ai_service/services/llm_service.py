from openai import OpenAI
from ai_service.config.settings import settings
from ai_service.config.logger import logger

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask(prompt: str) -> str:

    logger.info(f"Received prompt: {prompt}")

    response = client.chat.completions.create(
        model=settings.MODEL,
        messages=[
            {"role": "system", "content": "You are an AI teacher."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    return answer


class LLMService:
    pass