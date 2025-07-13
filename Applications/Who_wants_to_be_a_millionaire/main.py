questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

Prizes = ["1000$","2000$","3000$","4000$","5000$","6000$","7000$","8000$","9000$","10000$","11000$"]
i=0
for question in questions:
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])

    Answer = int(input("Enter the correct answer: "))

    if(question[5]==Answer):
        length=len(questions)
        print(f"Congrats!! you won {Prizes[i]}")
        i=i+1
        print("\n**************************************\n")

    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time")
        break    