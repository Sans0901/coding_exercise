# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
combined = name1 + name2
combined_str = combined.lower()
t = combined_str.count("t")
r = combined_str.count("r")
u = combined_str.count("u")
e = combined_str.count("e")
l = combined_str.count("l")
o = combined_str.count("o")
v = combined_str.count("v")
e = combined_str.count("e")

true = t+r+u+e
love = l+o+v+e

love_score = int(str(true) + str(love))
print(love_score)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}')


output :
Welcome to the Love Calculator!
What is your name? 
sanskruti
What is their name? 
kiran
40
Your score is 40, you are perfectly alright together.