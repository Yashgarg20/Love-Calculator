print("Welcome to the love calculator!")
name1=input("What is your name?\n")
name2=input("What is your name?\n")
string_combine=name1+name2
letter_in_lower_case=string_combine.lower()
t=letter_in_lower_case.count("t")
r=letter_in_lower_case.count("r")
u=letter_in_lower_case.count("u")
e=letter_in_lower_case.count("e")
true=t+r+u+e
l=letter_in_lower_case.count("l")
o=letter_in_lower_case.count("o")
v=letter_in_lower_case.count("v")
e=letter_in_lower_case.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if (love_score<10) or (love_score>90):
    print(f"Your love score is {love_score},you go together like coke and mentos")
elif(love_score>=40) and (love_score<=50):
    print(f"Your love score is {love_score},you are alright together") 
else:
    print(f"Your score is {love_score}")       


