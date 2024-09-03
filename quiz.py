questions = [
    {
        "prompt":"What is the capital of France?",
        "options":["A. paris","B. London","C. berlin","D. madrid"],
        "answer":"A"
    },
    {
        "prompt":"Which language is primarly spoken in Brazil?",
        "options":["A. Spanish","B. Portugal","C. English","D. French"],
        "answer":"B"
    },
    {
        "prompt":"What is the smallest prime number?",
        "options":["A. 1","B. 2","C. 3","D. 5"],
        "answer":"B"
    },
    {
        "prompt":"Who wrote 'to kill a Mokingbird'",
        "options":["A. Harper Lee","B. Mark Twain","C. J.K.Rowling","D. Ernest Hemingway"],
        "answer":"A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A,B,C,D): ").upper()
        if answer == question["answer"]:
            print("Correct!!!\n")
            score += 1
        else:
            print("Wrong, correct answer was", question["answer"], "\n")

    print(f"you got {score} out of {len(questions)} question correct.")

run_quiz(questions)