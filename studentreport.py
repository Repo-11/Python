student_marks = {
    "chandu":87,
    "kallal" :60,
    "malli" :45,
    "chanchal" : 96,
    "rahul" : 76,
    "kumar":55
    
    }

def grade(a):
    if a >= 90:
        return("excellent")
    elif a>=80 and a <90:
        return("Very good")
    elif a>=70 and a <80: 
        return("Good")
    elif a>=60 and a <70: 
        return("acceptable")
    elif a>=50 and a <60:  
        return("okish") 
    else:
        return("Fail") 
        
               


for i in student_marks:
    print(f"{i} = {grade(student_marks[i])}")
    