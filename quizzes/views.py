from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

from users.models import User
from .models import Quiz, Question, Answer

def index(request):
    return render(request, 'quizzes/quiz_index.html')

def dashboard(request):
    # if 'user_id' not in request.session:
    #     return redirect('/users/register')       
    context = {
        'all_quizzes': Quiz.objects.all(),
    }
    return render(request, 'quizzes/dashboard.html', context)

@login_required
def quiz_info(request, quiz_id):
    user = request.user
    context = {
        'this_user': User.objects.get(id=user.id),
        'this_quiz': Quiz.objects.get(id=quiz_id)
    }
    return render(request, 'quizzes/Quiz_info.html', context)

def create_score(request, quiz_id):
    if request.method != "POST":
        return redirect('/')
    # Insert answer validator
    # redirect if errors
    else:
        if 'user_id' in request.session:
            this_quiz = Quiz.objects.get(id=quiz_id)
            total_questions = 0
            score = 0
            for question in this_quiz.has_questions.all():
                total_questions+= 1
                print(question.id)
                print(request.POST['question_'+str(question.id)])
                if request.POST['question_'+str(question.id)] == 'True':
                    score += 1
                else:
                    score += 0
            user = User.objects.get(id=request.session['user_id'])
            quiz = Quiz.objects.get(id=quiz_id)
            # Result.objects.create(score=score, creator=user, quiz=quiz)
            print(request.POST)
            print(score)
            print(total_questions)
        return redirect('/quiz/result')

def result(request):
    # incomplete
    return HttpResponse('results go here')
# Create your views here.

def randomizer(request):
    context = {
        "blogs": Blog.objects.order_by('?')[0],
    }
    return render(request, 'randomizer.html', context)
