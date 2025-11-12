

## 🧮 3. `puzzle_generator.py`

import random

DIFFICULTIES = {
    "Easy": (1, 10),
    "Medium": (10, 50),
    "Hard": (50, 100)
}

OPERATIONS = ["+", "-", "*"]

def generate_puzzle(level):
    """Generates a math problem based on difficulty."""
    low, high = DIFFICULTIES[level]
    a, b = random.randint(low, high), random.randint(low, high)
    operation = random.choice(OPERATIONS)
    question = f"{a} {operation} {b}"
    answer = eval(question)
    return question, answer
