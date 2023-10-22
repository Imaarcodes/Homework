#recursive function #1


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


x = 3
print("The factorial of", x, "is", factorial(x))

#recursive funtion #2


def the_right_grade(trg):
    if trg == 4.75:
        return "good job!"
    else:
        return ("You are ", 4.75-trg, " behind!")

trg = 3
print("You are ", 4.75-trg, " behind!")