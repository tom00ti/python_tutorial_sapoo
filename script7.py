class Student:
    def __init__(self, name, math, japanese, english, science, society):
        self.name =name
        self.math = math
        self.japanese = japanese
        self.english = english
        self.science = science
        self.scociety = society
    
    def avarage_score(self):
        avg = (self.math+self.japanese+self.english+self.science+self.scociety)/5
        return avg
    
student_1 = Student("斎藤そうま",82,74,60,92,72)
s1_avg = student_1.avarage_score()

student_2 = Student("田中かえで",75,78,80,85,68)
s2_avg = student_2.avarage_score()

print(s2_avg)