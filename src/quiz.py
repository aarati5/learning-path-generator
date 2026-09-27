import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz(module_title: str, module_description: str) -> list:
    system_prompt = """You are a quiz generator. Create a short multiple-choice quiz to test understanding of a topic.

Return ONLY a valid JSON array, no other text, in this exact format:
[
  {"question": "question text", "options": ["A", "B", "C", "D"], "correct_index": 0}
]

Rules:
- Create exactly 3 questions
- correct_index is 0-based (0 = first option)
- Questions should test real understanding, not just memorization
"""

    model = genai.GenerativeModel(
        model_name="gemini-3.8-flash",
        system_instruction=system_prompt
    )

    prompt = f"Module: {module_title}\nDescription: {module_description}"
    response = model.generate_content(prompt)
    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        print("Warning: Could not parse quiz response.")
        print(raw_text)
        return []


def run_quiz(questions: list) -> float:
    if not questions:
        return 0.0

    correct_count = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"  {idx+1}. {option}")

        answer = input("Your answer (1-4): ").strip()
        try:
            chosen_index = int(answer) - 1
            if chosen_index == q['correct_index']:
                print("Correct!")
                correct_count += 1
            else:
                correct_answer = q['options'][q['correct_index']]
                print(f"Incorrect. Correct answer: {correct_answer}")
        except (ValueError, IndexError):
            print("Invalid input, marked as incorrect.")

    score = correct_count / len(questions)
    return score