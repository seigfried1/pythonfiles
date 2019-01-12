students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
"""Finds the students with second lowest grades"""
marks_list = []
for i, j in students:
	marks_list.append(j)
marks_list.sort(reverse=True)

desired_num = 0
lowest_num = marks_list[-1]
for i in range(len(marks_list)-1,0,-1):
	if marks_list[i] > lowest_num:
		desired_num+= marks_list[i]
		break
student_names = []
for i, j in students:
	if j == desired_num:
		student_names.append(i)
student_names.sort()
for i in student_names:
	print(i)
