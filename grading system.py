 
score = float(input("Enter the student's score (0-100): "))
    
    
if score >= 90 and score <= 100:
        grade = 'A'
elif score >= 80 and score < 90:
        grade = 'B'
elif score >= 70 and score < 80:
        grade = 'C'
elif score >= 60 and score < 70:
        grade = 'D'
elif score >= 0 and score < 60:
        grade = 'F'
else:
        grade = "Invalid score"
    
    
print(f"The student's grade is: {grade}")
