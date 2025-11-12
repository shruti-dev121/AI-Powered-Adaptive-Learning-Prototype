import time

def ask_question(question, answer):
    """Ask a question and record correctness and response time."""
    start = time.time()
    try:
        user_answer = int(input(f"Solve: {question} = "))
    except ValueError:
        print("Invalid input! Counting as incorrect.")
        return False, 0
    
    end = time.time()
    correct = (user_answer == answer)
    response_time = round(end - start, 2)
    
    if correct:
        print(f"✅ Correct! ({response_time}s)\n")
    else:
        print(f"❌ Wrong! Correct answer: {answer} ({response_time}s)\n")
    
    return correct, response_time
