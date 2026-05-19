def ask_question(question, correct_answer):
    print(question)
    user_answer = input("Your Answer: ")

    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The answer was {correct_answer}\n")
        return False
    
score = 0 
questions_total = 3

question1 = ask_question("What language are we learning", "python")
question2 = ask_question("What does CLI stand for?", "command line interface")
question3 = ask_question("What function prints output to the terminal?", "print")

if question1:
    score += 1
if question2:
    score += 1
if question3:
    score += 1

print(f"You scored {score} out of {questions_total}")