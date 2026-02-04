class Student:
    def __init__(self, hrno):
        self.hrno = hrno
        self.seat_x = 0
        self.seat_y = 0
        self.question_id = 1
        self.status = 1

students = []
for i in range(101):
    new_student = Student(i)
    students.append(new_student)

    
seats = []
for i in range(7):
    seats_row = []
    for j in range(6):
        seats_row.append(0)
    seats.append(seats_row)
    
class Series:
    def __init__(self, question_series = 1, question_counts = 4):
        self.question_series = question_series
        self.question_count = question_counts
        
    def question_address(self, question_id):
        return(str(self.question_series) + "/questions/q" + str(question_id) + ".jpg")
        
    def answer_address(self, question_id):
        return(str(self.question_series) + "/answers/a" + str(question_id) + ".jpg")
        
    def hint_address(self, question_id):
        return(str(self.question_series) + "/hints/h" + str(question_id) + ".jpg")
        

series = Series()        

class Hint:
    def __init__(self, hrno, question_id, content):
        self.hint_id = ""
        self.hrno = hrno
        self.question_id = question_id
        self.content = content
        self.good_students = set()
        self.good_count = 0
        
hints = []