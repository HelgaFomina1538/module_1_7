#Дополнительное практическое задание по модулю: "Базовые структуры данных."
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score_0 = float(sum(grades[0])/len(grades[0]))
average_score_1 = float(sum(grades[1])/len(grades[1]))
average_score_2 = float(sum(grades[2])/len(grades[2]))
average_score_3 = float(sum(grades[3])/len(grades[3]))
average_score_4 = float(sum(grades[4])/len(grades[4]))
students_list: list[str] = sorted(list(students))
average_student_score = {students_list[0] : average_score_0, students_list[1] : average_score_1,
                         students_list[2] : average_score_2, students_list[3] : average_score_3,
                         students_list[4] : average_score_4}
print(average_student_score)