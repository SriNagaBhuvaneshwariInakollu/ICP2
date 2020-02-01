stu = input("Please enter the number of students: ")
stu = int(stu)
weightsLBs = []
weightsKGs = []
for n in range(stu):
        w_lb = float(input("Enter the weight of student in lbs>>"))
        weightsLBs.append(w_lb)

weightsKGs = [weightsLBs[x]*0.453592 for x in range(stu)]

print(weightsKGs)