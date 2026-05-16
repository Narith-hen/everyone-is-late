# the solution one
student_scores = [45, 78, 90, 56, 88, 34, 67]
for score in student_scores:
    print(score)

# the solution two and three
total = 0
count = 0
student_scores = [45, 78, 90, 56, 88, 34, 67]
for score in student_scores:
    total += score
    count += 1
average = total/count
print("Total scores:",total)
print("Average of students scores:",round(average, 2))

# the solution four and five
student_scores = [45, 78, 90, 56, 88, 34, 67]
for score in student_scores:
    if score >= 50:
        print("Score that student passed:",score)

    else:
        print("Score that student failed:",score)

# the solution six
student_scores = [45, 78, 90, 56, 88, 34, 67]
for score in student_scores:
    if score < 50:
        newScore = score + 5
        print(newScore)

# the solution seven
student_scores = [45, 78, 90, 56, 88, 34, 67]
for score in student_scores:
    if score > 80:
        print("The student who recieve certificate:",score)

# the solution eight
student_scores = [45, 78, 90, 56, 88, 34, 67]
scores_to_grade = []
for i in range(len(student_scores)):
    if student_scores[i] < 50:
        scores_to_grade.append("F")
    elif student_scores[i] < 70 and student_scores[i] >= 50:
        scores_to_grade.append("D")
    elif student_scores[i] < 80 and student_scores[i] >= 70:
        scores_to_grade.append("C")
    elif student_scores[i] < 90 and student_scores[i] >= 80:
        scores_to_grade.append("B")
    else:
        scores_to_grade.append("A")
print(student_scores)
print(scores_to_grade)
