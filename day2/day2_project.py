def ask_question(question, hint, correct_answer,):
    print(question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == correct_answer.lower():
        print("You Dunnit!\n")
        return True
    else:
        print(f"Hint: {hint}\n")
        second_answer = input("Try again: ")

        if second_answer.lower() == correct_answer.lower():
            print("You Dunnit!\n")
            return True
    
        else:
            print(f"Wrong! The Answer was {correct_answer}\n")
            return False
    
score = 0 
questions_total = 5

question1 = ask_question("What does AGI stand for?","exceeding human capabilities","Artificial General Intelligence")
question2 = ask_question("What does API stand for?","digital waiter","Application Programming Interface")
question3 = ask_question("What languages is AI written in the most?","not java","python")
question4 = ask_question("do all industries need AI?","?","maybe")
question5 = ask_question("what is the basic unit of text (a word or part of a word) processed by LLMs?","like a coin","Token")

if question1:
    score += 1
if question2:
    score += 1
if question3:
    score += 1
if question4:
    score += 1
if question5:
    score += 1

print(f"you scored {score} out of {questions_total}")

if score >= 4:
    print("great job")
if score >= 2:
    print("okay job")
else:
    print("learn more, try again")
    