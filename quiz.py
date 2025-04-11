# Simple Quiz App in Python

# List of quiz questions
quiz = [{"question": "What is the capital of France?","options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],"answer": "B"}, {"question": "What is 5 + 7?","options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"}, {"question": "Which planet is known as the Red Planet?","options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],"answer": "C"}, {"question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],"answer": "B"}]

def run_quiz():
    score = 0
    print("\n📚 Welcome to the Quiz Application!\n")
    print("Rules:")
    print("- Each question has 4 options.")
    print("- Enter the option (A,B,C,D) as your answer")
    print("Press Enter to Start!\n")

    for i, q in enumerate(quiz, start=1):
        print(f"Question{i}: {q['question']}")
        for o in q['options']:
            print(o)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")

    print(f"🎉🎉 Quiz Completed! You scored {score} out of {len(quiz)}.")

if __name__ == "__main__":
    run_quiz()
    
