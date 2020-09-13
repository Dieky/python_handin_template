import random
import pprint
import matplotlib.pyplot as plt

class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        # In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
        """Initialize title, the author, and the chapters."""
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r,%r,%r)' % (self.name, self.gender, self.data_sheet, self.image_url)

# In student create a method: get_avg_grade()
    def get_avg_grade(self):
        total = 0
        divident = 0
        for x in self.data_sheet:
            if(x.grade != -1):
                total += x.grade
                divident += 1
        result = total / divident
        return result

    def get_total_study_progression(self):
        ETCS_total = 0
        for x in self.data_sheet:
            ETCS_total += int(x.ETCS)
        progress_status = round(ETCS_total / 150 * 100,2)
        return progress_status

class DataSheet():
        # A student has a data_sheet and a data_sheet has multiple courses in particular order

    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)

    def __init__(self, courses=[]):
        self.courses = courses

# In DataSheet create a method to get_grades_as_list()
    def get_grades_list(self):
        return self.courses


class Course():
    # Each course has name, classroom, teacher, ETCS and optional grade if course is taken.

    def __repr__(self):
        return 'Course(%r, %r,%r,%r,%r)' % (self.name, self.classroom, self.teacher, self.ETCS, self.grade)

    def __init__(self, name, classroom, teacher, ETCS, grade=-1):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

# Create a function that can generate n number of students with random:
# name, gender, courses (from a fixed list of course names), grades, img_url


def create_n_students(number):
    list_of_students = []
    list_of_names = ["Hans", "Peter", "Helga", "Yrsa", "Lars","Thomas","Karen","Conny"]
    possible_genders = ["Mand", "Kvinde"]
    course1 = Course("Math", 1, "Steen Brandt", 15)
    course2 = Course("Dansk", 2, "Mogens Blisdorf", 20)
    course3 = Course("English", 2, "Trine Haremose", 10)
    list_of_courses = [course1, course2, course3]
    for x in range(number):
        final_course_list = []
        for y in range(len(list_of_courses)):
            result = random.randint(0, 1)
            if(result == 1):
                final_course_list.append(list_of_courses[y])
        # Added +"_"+str(x) to see a different ID on names
        name = list_of_names[random.randrange(3)]+"_"+str(x)
        student = Student(name, possible_genders[random.randint(
            0, 1)], final_course_list, "www.website.com/profile/"+name)
        list_of_students.append(student)
    write_csv(list_of_students, "DELME.csv")

# Let the function write the result to a csv file
# with format stud_name, course_name, teacher, ects, classroom, grade, img_url


def write_csv(student_list, outfile):
    with open(outfile, 'w') as file_object:
        for student in student_list:
            for course in student.data_sheet:
                teacher = course.teacher
                course_name = course.name
                etcs = course.ETCS
                classroom = course.classroom
                if(course.grade == -1):
                    grade = "Incomplete"
                else:
                    grade = course.grade
                file_object.write("{},{},{},{},{},{},{}\n".format(
                    student.name, course_name, teacher, etcs, classroom, int(grade), student.image_url))


# Read student data into a list of Students from a csv file:
# loop through the list and print each student with name, img_url and avg_grade.
# sort the list by avg_grade
# create a bar chart with student_name on x and avg_grade on y-axis

def read_csv(file, outfile):
    student_list = []
    with open(file, "r") as file_obj:
        for line in file_obj.readlines():
            student_list.append((line.rstrip()))

    for student in student_list:
        result = student.split(",")
        # print(type(result))
        # student = Student(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        (name, course, teacher, ETCS, classroom, grade, image_url) = result
        print(name, course, teacher, ETCS, classroom, grade, image_url)
    # print(content_list)


def create_n_complete_students(number):
    list_of_students = []
    list_of_names = ["Hans", "Peter", "Helga", "Yrsa", "Lotte", "Freja", "Birger",
                     "Sandra", "Bubber", "Morten", "Kenny", "Casper", "Frank", "Buckingham"]
    possible_genders = ["Mand", "Kvinde"]
    grade_list = [-3, 0, 2, 4, 7, 10, 12]
    course1 = Course("Math", 1, "Steen Brandt", 20)
    course2 = Course("Dansk", 2, "Mogens Blisdorf", 20)
    course3 = Course("English", 3, "Trine Haremose", 15)
    course4 = Course("Biology", 4, "Preben Dadelplukker", 10)
    course5 = Course("Fysik", 5, "Torben Boom", 7)
    list_of_courses = [course1, course2, course3, course4, course5]
    for x in range(number):
        final_course_list = []
        for y in range(len(list_of_courses)):
            result = random.randint(0, 1)
            if(result == 1):
                final_grade = grade_list[random.randint(0, len(grade_list)-1)]
                addCourse = Course(list_of_courses[y].name, list_of_courses[y].classroom,
                                   list_of_courses[y].teacher, list_of_courses[y].ETCS, final_grade)
                final_course_list.append(addCourse)
        # Added +"_"+str(x) to see a different ID on names
        name = list_of_names[random.randrange(len(list_of_names))]+"_"+str(x)
        student = Student(name, possible_genders[random.randint(
            0, 1)], final_course_list, "www.website.com/profile/"+name)
        list_of_students.append(student)
    return list_of_students


def write_complete_csv(student_list, outfile):
    """
    Writes a csv file to <outfile> from the given <student_list>. MUST be a complete list which is gained from calling create_n_complete_students(number)
    """
    with open(outfile, "w") as file_object:
        for student in student_list:
            for course in student.data_sheet:
                file_object.write(
                    "{},{},{},{},{},{},{},{}\n".format(student.name, student.gender,
                                                       student.image_url, course.name, course.teacher, course.classroom, course.ETCS, int(course.grade)))


def write_complete_student():
    """
    Writes all of the attributes of a student. Students may appear more than once due to multiple courses
    """
    list_to_write = create_n_complete_students(10)
    write_complete_csv(list_to_write, "DELME2.csv")

# opg 8
def create_students_from_csv_file():
    student_dict = {}
    with open("DELME2.csv", "r") as file_object:
        for line in file_object.readlines():
            course_list = []
            (student_name, gender, image_url, course_name,
             teacher, classroom, ETCS, grade) = line.split(",")
            course = Course(course_name, classroom, teacher, ETCS, int(grade))
            course_list.append(course)
            if student_name not in student_dict.keys():
                student_dict[student_name] = Student(
                    student_name, gender, course_list, image_url,)
            else:
                current_student = student_dict[student_name]
                new_course_list = []
                new_course_list.append(course)
                for x in range(0, len(current_student.data_sheet)):
                    grade = int(current_student.data_sheet[x].grade)
                    new_course = Course(current_student.data_sheet[x].name, current_student.data_sheet[x].teacher,
                                        current_student.data_sheet[x].classroom, current_student.data_sheet[x].ETCS, grade)
                    new_course_list.append(new_course)
                student = Student(current_student.name, current_student.gender,
                                  new_course_list, current_student.image_url)
                student_dict[student_name] = student
    final_list = []
    for student in student_dict.values():
        final_list.append(student)
    return final_list

# loop through the list and print each student with name, img_url and avg_grade.

# 8a
def print_student_average(student_list):
    for student in student_list:
        print(student.name)
        print(student.image_url)
        print(student.get_avg_grade(), "\n")

# 8b
def sort_students(student_list):
    for f in sorted(student_list, key=Student.get_avg_grade):
        print("Navn på student: {} - Gennemsnit: {}".format(f.name,f.get_avg_grade()))

# 8c
def print_barchart(student_list):
    plot_list_student_name = []
    plot_list_student_avg_grade = []
    for student in student_list:
        plot_list_student_name.append(student.name)
        plot_list_student_avg_grade.append(student.get_avg_grade())
    plt.bar(plot_list_student_name, plot_list_student_avg_grade, width=0.5, align='center') # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
    #plt.ticklabel_format(useOffset=False)
    # plt.axis([0, max(ages) + 10, 0, max_y_val+500]) #axis(x-min, x-max, y-min, y-max)
    # title = 'Distribution of {} CPH Citizens in {}'.format(sum(no_citicens), 2015)
    #plt.title(title, fontsize=12)
    plt.xlabel("Student", fontsize=20)
    plt.ylabel("Average grade", fontsize=20)
    # plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()


def print_grouped_students_progres(student_list):
    plot_list_student_progress = [20,57,19,13,22,74,34,55,76,91]
    study_progress_intervals = [10,20,30,40,50,60,70,80,90,100]
    for student in student_list:
        prog = student.get_total_study_progression() / 10
        study_progress_intervals[prog].
        plot_list_student_progress.append(student.get_total_study_progression())
    plt.bar(study_progress_intervals, plot_list_student_progress, width=0.5, align='center') # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
    plt.xlabel("Study progress", fontsize=20)
    plt.ylabel("Number of students", fontsize=20)
    plt.show()

def test_progres(student_list):
    for student in student_list:
        print("{}'s total progression: {}%".format(student.name,student.get_total_study_progression()))


if __name__ == "__main__":
    # write_complete_student()
    student_list = create_students_from_csv_file()
    #sort_students(student_list)
    # print_student_average(student_list)
    #print_barchart(student_list)
    #test_progres(student_list)
    print_grouped_students_progres(student_list)



