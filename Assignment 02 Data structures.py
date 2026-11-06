age_list = [24, 25, 26, 27, 28]
name_list = ["Arun", "Divya", "Kiran", "Meera", "Rahul"]

# a. Append:
name_list.append("Yazhini")
print(name_list)   # ['Arun', 'Divya', 'Kiran', 'Meera', 'Rahul', 'Yazhini']

# b. Insert: 
age_list.insert(2, 30)
print(age_list)    # [24, 25, 30, 26, 27, 28]

# c. Remove:
name_list.remove("Yazhini")
print(name_list)   # ['Arun', 'Divya', 'Kiran', 'Meera', 'Rahul']

# d. Pop: 
age_list.pop()
print(age_list)    # [24, 25, 30, 26, 27]

# e. Extend: 
age_list.extend([29, 30, 26])
print(age_list)    # [24, 25, 30, 26, 27, 29, 30, 26]

# f. Descending sort
age_list.sort(reverse=True)
print(age_list)    # [30, 30, 29, 27, 26, 26, 25, 24]

# g. Max, Min, Sum
print("Max age:", max(age_list))   # 30
print("Min age:", min(age_list))   # 24
print("Sum of ages:", sum(age_list))  # 217

print(name_list[0])      # a. first element -> Arun
print(name_list[-1])     # b. last element  -> Rahul
print(name_list[2:5])    # c. index 2 to 4  -> ['Kiran', 'Meera', 'Rahul']
print(name_list[::-1])   # d. reverse       -> ['Rahul', 'Meera', 'Kiran', 'Divya', 'Arun']

# a. Create
student_marks = {
    "Arun": 78,
    "Divya": 85,
    "Kiran": 92,
    "Meera": 67,
    "Rahul": 74
}

# b. 
print(student_marks["Kiran"])    # 92

# c. 
student_marks["Janani"] = 80

# d. 
student_marks["Arun"] = 82

# e. keys(), values(), items()
print(student_marks.keys())     # dict_keys(['Arun', 'Divya', 'Kiran', 'Meera', 'Rahul', 'Janani'])
print(student_marks.values())   # dict_values([82, 85, 92, 67, 74, 80])
print(student_marks.items())    # dict_items([('Arun', 82), ('Divya', 85), ...])

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print(my_set)    # {'a', 'e', 'i', 'o', 'u'} 

try:
    my_set[4] = 's'
except TypeError as e:
    print("Error:", e)

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print("Union:", set1 | set2)               # {1, 2, 3, 5, 7, 8, 9, 10}
print("Intersection:", set1 & set2)        # {3, 5}

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Please enter a value between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! Keep up the great performance.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")