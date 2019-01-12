students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
"""Finds the students with second lowest grades"""        
min_value = min([i[1] for i in students])
second_min_value = min([i[1] for i in students if i[1] > min_value])
ans = [i[0] for i in students if i[1] == second_min_value]
for i in sorted(ans):
    print(i)