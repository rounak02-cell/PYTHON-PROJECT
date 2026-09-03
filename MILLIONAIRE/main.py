# List of questions. Each question is a list containing:
# [question_text, option_a, option_b, option_c, option_d, correct_answer_number]
# correct_answer_number: 1=a, 2=b, 3=c, 4=d
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

# Prize money for each question level (index 0 = prize for question 1, and so on)
prizes = [100000, 320000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

# 'i' tracks which prize level the player is currently on
i = 0

# Loop through each question one at a time
for question in questions:
    # Print the question text
    print(question[0])
    # Print the four answer options (a, b, c, d)
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Ask the player to choose an answer (1-4 corresponding to a-d)
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))

    # Compare the player's choice with the correct answer stored at index 5
    if question[5] == a:
        print("Correct Answer")
    else:
        # Wrong answer ends the game immediately
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break  # exits the for loop, stopping the game

    # If correct, show how much money the player has won so far
    print(f"You won {prizes[i]}")

    # Move to the next prize level for the next question
    i += 1