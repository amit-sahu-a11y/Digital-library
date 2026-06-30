import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class GenerationService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_answer(self, query, context):

        prompt = f"""
You are an AI tutor.

Use ONLY the information provided in the context.

Rules:
1. If the answer is not present in the context, reply:
   "I couldn't find this information in the uploaded documents."
2. Explain the answer clearly.
3. Use short paragraphs.
4. Do not invent information.
5. Do not mention the context.

Context:
{context}

Question:
{query}

Answer:
"""

        response = self.model.generate_content(prompt)

        return response.text