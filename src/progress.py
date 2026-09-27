import json
import os

STORAGE_FILE = "progress.json"

def load_progress() -> dict:
    if not os.path.exists(STORAGE_FILE):
        return {"goal": None, "level": None, "modules": [], "current_index": 0, "scores": []}
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def save_progress(data: dict):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def start_new_path(goal: str, level: str, modules: list):
    data = {
        "goal": goal,
        "level": level,
        "modules": modules,
        "current_index": 0,
        "scores": []
    }
    save_progress(data)
    return data

def record_score(score: float):
    data = load_progress()
    data["scores"].append(score)

    # Adaptive logic: low score = repeat module, high score = advance
    if score >= 0.7:
        data["current_index"] += 1
        message = "Great job! Moving to the next module."
    else:
        message = "Score below 70% — recommend reviewing this module again before advancing."

    save_progress(data)
    return message

def get_current_module():
    data = load_progress()
    modules = data.get("modules", [])
    idx = data.get("current_index", 0)

    if idx >= len(modules):
        return None
    return modules[idx]

def get_progress_summary() -> str:
    data = load_progress()
    modules = data.get("modules", [])
    idx = data.get("current_index", 0)
    scores = data.get("scores", [])

    if not modules:
        return "No learning path created yet."

    lines = [f"Goal: {data['goal']}", f"Progress: Module {idx+1} of {len(modules)}"]
    if scores:
        avg_score = sum(scores) / len(scores)
        lines.append(f"Average quiz score: {avg_score*100:.0f}%")
    return "\n".join(lines)