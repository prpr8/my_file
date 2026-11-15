low = 1
high = 100

while low <= high:
    guess = (low + high) // 2
    print("Think of a number and i'll guess it!")
    print(f"guess is {guess}")
    feedback = input("enter h for higher, l for lower, c for correct: ")
    if feedback == "h":
        low = guess + 1
    elif feedback == "l":
        high = guess - 1
    elif feedback == "c":
        print("your no. is ", guess)
        break
    else:
        print("invalid input")
else:
    print("Feedback was inconsistent, no number left to guess")       
