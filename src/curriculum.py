import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_learning_path(goal: str, current_level: str) -> list:
    system_prompt = """You are a curriculum designer. Create a structured learning path.

Return ONLY a valid JSON array, no other text, in this exact format:
[
  {"module": "Module title", "description": "What this module covers and why it matters", "estimated_hours": 3}
]

Rules:
- Create 4 to 6 modules, ordered from foundational to advanced
- Each module should be specific and actionable, not vague
- Base the difficulty and starting point on the user's current level
"""

    model = genai.GenerativeModel(
        model_name="gemini-3.8-flash",
        system_instruction=system_prompt
    )

    prompt = f"Goal: {goal}\nCurrent level: {current_level}"
    response = model.generate_content(prompt)
    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        print("Warning: Could not parse curriculum response.")
        print(raw_text)
        return []