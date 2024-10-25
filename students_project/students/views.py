from django.shortcuts import render
import random

# Create your views here.
def get_random_students():
    first_names = ['Andria', 'Nika', 'Giorgi', 'Levani', 'Tato', 'Mariami', 'Qeti', 'Otari', 'Davit', 'Irakli','Zurab', 'Avtandil', 'Tamaz', 'Mikheil', 'Anano', 'Elene']
    last_names = ['Zazashvili', 'Managadze', 'tchikadze', 'Beglarishvili', 'Burdiladze', 'barnovi', 'Nikolashvili', 'Aladashvili', 'Abashidze', 'Mgeladze', 'meskhi', 'nozadze', 'oboladze', 'obolashvili']
    students = []
    for i in range(100):
        student = {
            'Name': random.choice(first_names),
            'Surname' : random.choice(last_names),
            'GPA' : round(random.uniform(1.0, 4.0),2),
            'Course': random.randint(1,4)
        }
        students.append(student)
    return students

def main_page_view(request):
    students = get_random_students()
    choice = random.choice(students)
    context = {
        'student': choice
    }
    return render(request, 'main_page.html', context)

def students_page_view(request):
    students = get_random_students()
    context = {
        'students' : students
    }
    return render(request, 'students_page.html', context)