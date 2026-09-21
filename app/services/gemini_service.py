import os
from google import genai

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not configured. Add it to .env for AI chat.")
        self.client = genai.Client(api_key=api_key)
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    def answer(self, question: str, context: str) -> str:
        prompt = f"""You are CampusSphere AI, a student database assistant.
Use ONLY the supplied database context. Never invent records.
If the context is insufficient, say that the information is not available.
Keep answers concise and useful. Use bullets when listing multiple students.

DATABASE CONTEXT:
{context}

USER QUESTION:
{question}
"""
        response = self.client.models.generate_content(model=self.model, contents=prompt)
        return response.text or "I could not generate an answer."
