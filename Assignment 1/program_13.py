# Program 13: Percentage of marks
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(4)]
percentage = sum(marks) / 4
print("Percentage:", percentage)