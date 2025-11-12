from puzzle_generator import generate_puzzle
from tracker import ask_question
from adaptive_engine import update_difficulty_ml

def show_summary(name, performance):
    total = len(performance)
    correct = sum(p[1] for p in performance)
    avg_time = sum(p[2] for p in performance) / total
    accuracy = correct / total * 100

    print("\n📊 SESSION SUMMARY")
    print(f"👤 Player: {name}")
    print(f"✅ Accuracy: {accuracy:.2f}%")
    print(f"⏱️ Average Time: {avg_time:.2f}s")

    if accuracy > 80:
        print("🌟 Recommended next level: Hard")
    elif accuracy > 50:
        print("👍 Recommended next level: Medium")
    else:
        print("💪 Keep practicing at Easy level")


def main():
    print("🎮 Welcome to Math Adventures!")
    name = input("Enter your name: ")
    level = input("Choose starting level (Easy/Medium/Hard): ").capitalize()

    performance = []
    correct_results = []
    times = []

    for i in range(10):
        print(f"\n--- Puzzle {i+1} ---")
        question, answer = generate_puzzle(level)
        correct, time_taken = ask_question(question, answer)

        performance.append((level, correct, time_taken))
        correct_results.append(correct)
        times.append(time_taken)

        # Update difficulty using ML
        level = update_difficulty_ml(level, correct_results, times)

    show_summary(name, performance)


if __name__ == "__main__":
    main()
