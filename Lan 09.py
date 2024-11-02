import json
def form():
    code =[]
    title =[]
    credit_hours = []
    semester = []
    for i in range(4):
        if i == 0:
            code.append("Code")
            title.append("Title")
            credit_hours.append("Credit Hours")
            semester.append("Semester")
        elif (i == 1):
            code.append("001")
            title.append("DLD")
            credit_hours.append("3")
            semester.append("2")
        elif (i == 2):
            code.append("002")
            title.append("PF")
            credit_hours.append("3")
            semester.append("1")
        else:
            code.append("003")
            title.append("ICT")
            credit_hours.append("3")
            semester.append("4")
        
            
        
            
    
       
        
        
            
    
    for i in range(4):       
        header = f'{code[i].ljust(8)}{title[i].ljust(40)}{credit_hours[i].ljust(15)}{semester[i].ljust(10)}'
        print(header)
form()
        
