score = int(input("Enter your score (0-100): "))  

if score >= 0 and score <= 60:  # F grade condition  
    grade = 'F'  
elif score > 60 and score <= 70:  # D grade condition  
    grade = 'D'  
elif score > 70 and score <= 80:  # C grade condition  
    grade = 'C'  
elif score > 80 and score <= 90:  # B grade condition  
    grade = 'B'  
elif score > 90 and score <= 100:  # A grade condition  
    grade = 'A'  
else :  # Invalid score condition  
    grade = 'Invalid score'  

print(f"Your grade is: {grade}")  