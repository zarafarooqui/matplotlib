import matplotlib.pyplot as plt

student_names = ["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
students_marks =[35,50,20,45,25,40,25,40]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def line_chart():
    plt.plot(student_names , students_marks, marker = "^", ms = 12 , mec = 'r', linestyle = "dotted" , linewidth = 7 , color = "green")
    plt.title("Students marks graph")
    plt.xlabel("Students names")
    plt.ylabel("Students marks")
    plt.show()

line_chart()

def bargraph():
    plt.bar(student_names  , marks_perc )
    plt.title("percentage bar graph")
    plt.xlabel("Students names")
    plt.ylabel("marks percentage")
    plt.show()