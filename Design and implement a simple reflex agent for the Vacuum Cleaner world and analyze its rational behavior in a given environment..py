environment = {'A':'dirty', 'B':'dirty'}
location = 'A'

while True:
    print("Agent in Room : ", location)
    print("Status : ", environment)

    if environment['A'] == 'clean' and environment['B'] == 'clean':
        print("Goal Achieved! both room are clean")
        break

    if environment[location] == 'dirty':
        print("room ", location, " is dirty")
        print("Action : Suck")
        environment[location] = 'clean'
    else:
        if location == 'A':
            print("Action : Move Right")
            location = 'B'
        else:
            print("Action : Move Left")
            location = 'B'
    print("-"*40)   
