#Write a program that: marks=[78,82,91] Add 95 Insert 80 at index 1 Remove 82 Sort the list Print the final list
marks = [78, 82, 91]
marks.append(95)
marks.insert(1, 80)
print(marks)
marks.pop(2)
marks.sort()
print(marks)