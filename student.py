name = input("Please enter student's full name: ")
age = int(input(f"Please enter {name.title()}'s age: "))
courseName = input(f"Please enter {name.title()}'s course name: ")
score1, score2, score3 = map(float, input("Please enter the scores: ").split())
average = (score1 + score2 + score3) / 3

print("Name: {}".format(name.title()))
print("Age:", age)
print("Average Score:", average)
if average >= 60:
    print("Passed!")
else:
    print("Failed!")
