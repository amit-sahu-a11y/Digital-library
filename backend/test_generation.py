from dotenv import load_dotenv
load_dotenv()

from app.services.generation_service import GenerationService

service = GenerationService()

context = """
Machine Learning is a branch of Artificial Intelligence.
It enables computers to learn from data without explicit programming.
"""

answer = service.generate_answer(
    "What is Machine Learning?",
    context
)

print(answer)