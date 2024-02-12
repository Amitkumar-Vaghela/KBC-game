import random

# Define questions and answers
questions = {
    "What is the capital of India?": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai", "B"],
    "Which planet is known as the Red Planet?": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn", "B"],
    "Who wrote 'To Kill a Mockingbird'?": ["A. Harper Lee", "B. J.K. Rowling", "C. Stephen King", "D. George Orwell", "A"],
    "What is the chemical symbol for water?": ["A. H2O", "B. CO2", "C. O2", "D. CH4", "A"],
    "Which is the longest river in the world?": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi", "A"],
    "Which country is known as the 'Land of the Rising Sun'?": ["A. China", "B. Japan", "C. South Korea", "D. Thailand", "B"],
    "Who painted the Mona Lisa?": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Claude Monet", "A"],
    "What is the largest mammal in the world?": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus", "B"],
    "What is the capital of Australia?": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane", "C"],
    "Which gas do plants primarily use for photosynthesis?": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen", "B"]  
}

def kbc():
    score = 0
    for question in questions:
        print(question)
        for option in questions[question][:4]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == questions[question][4]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            break
    print("You scored {} out of {}.".format(score, len(questions)))

# Main function to run the game
def main():
    print("Welcome to Kaun Banega Crorepati (KBC)!")
    print("Answer the following questions to win.")
    kbc()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
