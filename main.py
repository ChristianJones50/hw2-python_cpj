# Author: Christian Jones
# Collaborator: N/A

def getGradePoint(grade):
  if grade == "A":
    gradepoint = 4.0
  elif grade == "A-":
    gradepoint = 3.67
  elif grade == "B+":
    gradepoint = 3.33
  elif grade == "B":
    gradepoint = 3.0
  elif grade == "B-":
    gradepoint = 2.67
  elif grade == "C+":
    gradepoint = 2.33
  elif grade == "C":
    gradepoint = 2.0
  elif grade == "D":
    gradepoint = 1.0
  else:
    gradepoint = 0.0
  return gradepoint

def run():
  grade = input("Enter your course 1 grade letter: ")
  gradepoint1 = getGradePoint(grade)
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(grade)}")
  #
  grade = input("Enter your course 2 grade letter: ")
  gradepoint2 = getGradePoint(grade)
  credit2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint(grade)}")
  #
  grade = input("Enter your course 3 grade letter: ")
  gradepoint3 = getGradePoint(grade)
  credit3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint(grade)}")
  #
  gpa = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3)/(credit1 + credit2 + credit3)
  print(f"Your GPA is: {gpa}")




if __name__ == "__main__":
  run()