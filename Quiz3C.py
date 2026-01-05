# CS 303E Quiz 3C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: Adjacent Differences
def adjacentDifferences(lst):
    pass
    new_list = []
    for i in range(len(lst)-1):
        diff = lst[i+1] - lst[i]
        new_list.append(diff)
    return new_list

# Problem 2: Unequal Midterms
def computeCourseGrade(m1, m2, m3):
    pass
    if m1 >= m2 and m1 >= m3:
        course_grade = m1*.4 + (m2+m3)*.3
    elif m2 >= m1 and m2 >= m3:
        course_grade = m2*.4 + (m1+m3)*.3
    elif m3 >= m1 and m3 >= m2:
        course_grade = m3*.4 + (m1+m2)*.3
    return int(course_grade)

def getStudentGrades(grades):
    pass
    student_course_grades = []
    for student in grades:
        name = student[0]
        m1 = student[1]
        m2 = student[2]
        m3 = student[3]
        course_grade = computeCourseGrade(m1, m2, m3)
        student_course_grades.append([name, course_grade])
    return student_course_grades

if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(adjacentDifferences([29, 15, 13, 20, 21, 1, 29, 6, 27, 28, 1, 6]))
    # print(adjacentDifferences([2, 3]))
    # print(adjacentDifferences([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]))

    # print(computeCourseGrade(85, 79, 85))
    # print(computeCourseGrade(85, 92, 83))
    # print(getStudentGrades([["Hannah", 85, 79, 85], ["Eli", 85, 92, 83], ["Elena", 96, 95, 100]]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT