import os

from dotenv import load_dotenv
from groq import Groq


class LLM:
    load_dotenv()

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
