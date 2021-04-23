from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from .forms import PostForm, NewStudentsForm
from django.db.models import Count


# Create your views here.

def index(request):
    not_primary = "True"
    if request.method == 'POST':
        not_primary = "False"
        teacher_id = request.POST.get('teacher_id')
        room_id = request.POST.get('room_id')
        if teacher_id != '':
            if room_id != '':
                subject = Subject.objects.filter(created_by=teacher_id, pk=room_id)
                for item in subject:
                    if int(room_id) == int(item.pk):
                        if int(teacher_id) == int(item.created_by.pk):
                            return redirect('examination_room', teacher_id=teacher_id, room_id=room_id)
                    else:
                        return redirect('index')
    return render(request, 'main/index.html', {'not_primary':not_primary})

def examination_room(request, teacher_id, room_id):
    subject = get_object_or_404(Subject, pk=room_id)
    questions = subject.subject.all()
    if request.method == 'POST':
        form = NewStudentsForm(request.POST)
        if form.is_valid():
            student_by = form.save(commit=False)
            student_by.subject = subject
            student_by.save()

            for question in questions:
                slou = request.POST.get(f'exampleRadios{question.id}')
                if slou == 'option1':
                    data = Solutions(question=question, student_by=student_by, solution=question.answer_1)
                    data.save()
                elif slou == 'option2':
                    data = Solutions(question=question, student_by=student_by, solution=question.answer_2)
                    data.save()
                elif slou == 'option3':
                    data = Solutions(question=question, student_by=student_by, solution=question.answer_3)
                    data.save()
                elif slou == 'yes':
                    data = Solutions(question=question, student_by=student_by, solution='صح')
                    data.save()
                elif slou == 'no':
                    data = Solutions(question=question, student_by=student_by, solution='خطأ')
                    data.save()
            return redirect('index')
    else:
        form = NewStudentsForm()

    return render(request, 'main/examination_room.html', {'questions':questions, 'subject':subject, 'form':form,})



@login_required()
def teacher(request):
    subject = Subject.objects.filter(created_by=request.user).annotate(comments=Count('subject'))
    #  .annotate(comments=Count('posts')) دالة لحساب عدد الحقول من علاقة معينة
    if request.method == 'POST':
        name = request.POST.get('name')
        room = Subject(name=name, created_by=request.user)
        room.save()
        return redirect('teacher')
    context =  {
        'subject': subject,
        }
    return render(request, 'teacher/teacher.html', context)

@login_required()
def questions(request, teacher_id, room_id):
    subject = get_object_or_404(Subject, created_by=teacher_id, pk=room_id)
    questions = Questions.objects.filter(created_by=teacher_id, subject=room_id)
    context =  {
        'topic': subject,
        'questions':questions,
        }
    return render(request, 'teacher/questions.html', context)

@login_required()
def reply_questions(request, teacher_id, room_id):
    subject = get_object_or_404(Subject, pk=room_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.subject = subject
            question.created_by = request.user
            question.save()
            return redirect('questions', teacher_id=teacher_id, room_id=room_id)
    else:
        form = PostForm()
    context = {'form': form, 'subject':subject,}
    return render(request, 'teacher/reply_question.html', context)

@login_required()
def edit_questions(request, teacher_id, room_id, question_id):
    questions = Questions.objects.get(id=question_id)
    subject = get_object_or_404(Subject, pk=room_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=questions)
        if form.is_valid():
            question = form.save(commit=False)
            question.subject = subject
            question.created_by = request.user
            question.save()
            return redirect('questions', teacher_id=teacher_id, room_id=room_id)
    else:
        form = PostForm(instance=questions)
    context = {'form': form, 'subject':subject, 'questions':questions,}
    return render(request, 'teacher/edit_questions.html', context)

@login_required()
def delete_question(request, teacher_id, room_id, question_id):
    Questions.objects.get(id=question_id).delete()
    return redirect('questions', teacher_id=teacher_id, room_id=room_id)

@login_required()
def students(request, room_id):
    # students = Students.objects.filter(subject=room_id)
    subject = get_object_or_404(Subject, pk=room_id)
    questions = subject.subject_student.order_by("-created_dt").annotate(comments=Count('students'))
    context = {'students': questions}
    return render(request, 'teacher/students.html', context)

@login_required()
def solutions(request, students_id):
    solution = Solutions.objects.filter(student_by=students_id)
    context = {
        'solutions': solution,
        }
    return render(request, 'teacher/solutions.html', context)
