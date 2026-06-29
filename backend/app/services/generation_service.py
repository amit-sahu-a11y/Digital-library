import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class GenerationService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_answer(self, query, context):

        prompt = f"""
You are an AI Academic Assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply exactly:

"I couldn't find this information in the uploaded documents."

-------------------------
Context:

{context}

-------------------------

Question:

{query}

Answer:
"""

        response = self.model.generate_content(prompt)

        return response.text