# Personal Learning Path Generator

An AI-powered curriculum generator that creates a personalized, multi-module learning path for any goal, then adaptively adjusts progression based on quiz performance — advancing when you demonstrate understanding, and recommending review when you don't.

## Problem It Solves

Most learning roadmaps are static — the same path regardless of whether you actually understood the previous module. This tool closes that gap by embedding assessment directly into the learning flow: quiz performance determines whether you advance or repeat, creating genuine self-paced, evidence-based progression.

## How It Works

1. User specifies a learning goal and current skill level
2. Gemini API generates a structured, ordered curriculum (4-6 modules with descriptions and time estimates)
3. For the current module, a 3-question quiz is generated to test real understanding (not just recall)
4. Based on the score:
   - 70% or higher: advances to the next module
   - Below 70%: recommends reviewing the current module again
5. Progress (current module, quiz history, average score) persists across sessions in a local JSON file

## Tech Stack

- Language: Python
- LLM: Google Gemini API (gemini-3.8-flash)
- Core concept: Structured curriculum generation + quiz-based adaptive progression + persistent state

## Setup

1. Clone the repo and navigate into it

2. Create a virtual environment:

python -m venv venv
venv\Scripts\activate

3. Install dependencies:

pip install google-generativeai python-dotenv

4. Create a .env file with your Gemini API key:

GEMINI_API_KEY=your_key_here

Get a free key at https://aistudio.google.com/apikey

5. Run the program:

python main.py

## Usage

Choose from the menu:
1. Create new learning path (enter your goal and current level)
2. View progress (see current module and average quiz score)
3. Take quiz for current module (answer 3 questions, get instant scoring and an advance/review recommendation)
4. Exit

## Example

Goal: "Generative AI for beginners", Level: "beginner"

Generated curriculum (5 modules):
1. Foundations of Generative AI and Large Language Models
2. Prompt Engineering Essentials
3. Exploring Image and Multimodal AI Tools
4. Building Custom AI Assistants and No-Code Workflows
5. AI Ethics, Hallucinations, and Responsible Usage

After taking the Module 1 quiz and scoring below 70%, the system automatically recommended reviewing Module 1 again instead of advancing — demonstrating the adaptive progression logic in action.

## Architecture

main.py - menu-driven CLI loop, connects all components
src/curriculum.py - generates a structured, JSON-formatted learning path based on goal and skill level
src/quiz.py - generates module-specific quiz questions and evaluates user answers
src/progress.py - persistence layer; tracks current module, quiz scores, and applies the 70% advance/review threshold

## Future Improvements

- Integrate live web search to pull real, current course links for each module instead of relying on the model's own knowledge
- Support partial credit and per-topic weak-area identification instead of a single pass/fail threshold
- Add a web UI with progress visualization