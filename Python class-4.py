assigentment= int(input("enter your assignment mark:"))
test= int(input("Enter your test mark:"))
lab= int(input("Enter your lab mark:"))
final_score= (0.1*assigentment+0.7*test+0.2*lab)
if final_score>=90:
    grade="A"
    print("your final score is",final_score)
    print("grade",grade)
elif final_score>=80:
    grade="B"
    print("your final scoer",final_score)
    print("grade",grade)
elif final_score>=70:
    grade="C"
    print(" your final score", final_score)
    print("grade",grade)
elif final_score>=60:
    grade="D"
    print("your final score", final_score)
    print("grade",grade)
else:
    grade="F"
    print("your final score", final_score)
    print("grade", grade)