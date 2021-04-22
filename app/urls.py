from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher', views.teacher, name='teacher'),
    path('teacher/students/<int:room_id>', views.students, name='students'),
    path('teacher/students/<int:students_id>/solutions', views.solutions, name='solutions'),
    path('teacher/<int:teacher_id>/room_id/<int:room_id>', views.questions, name='questions'),
    path('teacher/<int:teacher_id>/room_id/<int:room_id>/reply', views.reply_questions, name='reply_questions'),
    path('teacher/<int:teacher_id>/room_id/<int:room_id>/question/<int:question_id>/edit/', views.edit_questions, name='edit_questions'),

    path('examination_room/<int:teacher_id>/room_id/<int:room_id>', views.examination_room, name='examination_room'),
    
]
