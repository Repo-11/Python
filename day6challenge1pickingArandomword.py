import random
word_list = ["ardvark","baboon" , "camel"]


chosen_word = random.choice(word_list)
display = []

for n in chosen_word:
    display.append("_")

print(display)

life = 0
t = True
while  t :
    guess = input("guess a letter : ").lower()

    i = 0

    for n in chosen_word:
        if n == guess:
            display[i] = guess



        i+=1
    print(display)
    if guess not in chosen_word:
        life += 1



    for n in display:
        if n == "_":
            t = True
        elif n!= "_":
            t = False

    if life>=5:
        t = False

    print(f" you have {5-life} life left!")

print("Game Over")
