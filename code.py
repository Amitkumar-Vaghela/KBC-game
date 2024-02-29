# KBC Game with AMIT Vaghela
print("Welcome to Kaun Banega Crorepati!\n")

questions_answers  = [
  {
    "question"  : "What is the name of Draco Malfoy's son?",
     "choice1"  : "Scorpius",
     "choice2"  : "Lucius",
     "choice3"  : "Diego",
     "choice4"  : "Severus",     
     "correct"  : "Scorpius"
  },
  
  {
    "question"  : "What creature does Dumbledore have as a pet?",
     "choice1"  : "Efreet",
     "choice2"  : "Fey",
     "choice3"  : "Troll",
     "choice4"  : "Basilisk",     
     "correct"  : "Basilisk"
  },
  
  {
    "question"  : "What is Voldemort's final horcrux?",
     "choice1"  : "A mirror",
     "choice2"  : "A snake",
     "choice3"  : "A brooch",
     "choice4"  : "Harry Potter",     
     "correct"  : "A snake"
  },
  
  {
    "question"  : "Who takes over as headmaster of Hogwarts after Dumbledore's death?",
     "choice1"  : "Voldemort",
     "choice2"  : "Narcissa Black",
     "choice3"  : "Professor Trelawny",
     "choice4"  : "Professor Snape",                    
     "correct"  : "Professor Snape"
  },
  
  {
    "question"  : "Who killed Deatheater Antonin Dolohov during the Battle of Hogwarts?",
     "choice1"  : "Professor Flitwick",
     "choice2"  : "Ron Weasley",
     "choice3"  : "Falling Debris",
     "choice4"  : "Hermione Granger",     
     "correct"  : "Professor Flitwick"
  }
  {
    "question"  : "current railway minister of the  india?",
     "choice1"  : "Mamata banarjee",
     "choice2"  : "Ram vilash",
     "choice3"  : "piyus gohel",
     "choice4"  : "Ashvini vaishnaw",     
     "correct"  : "Ashvini vaishnaw"
  }
]
score = 0

for item in questions_answers:
        print("\n", item["question"])
        print("Option A:\t" + item["choice1"])
        print("Option B:\t" + item["choice2"])
        print("Option C:\t" + item["choice3"])
        print("Option D:\t" + item["choice4"])
        user_choice  = input("Please type the correct answer:\n>>>>>\t")
        if user_choice.title() in item["correct"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer is : " + item["correct"])

print("Your score is: " + str(score))
print("You won Rs", 1000*(2**score)) # money gets doubled at each correct answer
print("Thanks for playing!")
