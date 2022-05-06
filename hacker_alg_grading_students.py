def gradingStudents(grades):

    total = []
    for i in grades:
        if i > 37:
            if 5-i%5 < 3:
                total.append(i+(5-i%5))
            else:
                total.append(i)
        else:
            total.append(i)
    return total
gr = [73, 67, 38, 33]
print(gradingStudents(gr))
