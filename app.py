import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from chainlit.playground.providers.openai import ChatOpenAI


print("all ok")

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

AsyncOpenAI(api_key=OPENAI_API_KEY)

print("client is created")