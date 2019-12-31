from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, logout, login
import subprocess
from . import models


def happy_new_year(request):

    return render(request, 'cloud/happy_new_year.html')


def signin(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['user'], password=request.POST['pass'],
        )
        if user and user.is_active == True:
            login(request, user)
            return redirect('/calc_eig')
        else:
            return render(
                request,
                'cloud/singin.html',
                {'message': 'Неверный логин или пароль'},
            )

    return render(request, 'cloud/singin.html')


def lera(request):
    return render(request, 'cloud/lerrrra.html')


def signup(request):
    if request.method == 'POST':
        try:
            user = models.User.objects.create_user(
                username=request.POST['user'], password=request.POST['pass'],
            )
            user.save()
        except:
            pass

        return redirect('/signin')

    return render(request, 'cloud/signup.html')


def calc_eig(request):
    # send request to db
    tasks = models.Tasks.objects.filter(user=request.user)
    done_tasks = [task for task in tasks if task.done]
    undone_tasks = [task for task in tasks if not task.done]
    # the end
    return render(
        request,
        'cloud/task.html',
        {'done_tasks': done_tasks, 'undone_tasks': undone_tasks},
    )


def save_task(request):
    task = models.Tasks()
    task.user = request.user
    for attr in request.POST:
        task.__setattr__(attr, request.POST.get(attr))
    task.save()

    tasks = models.Tasks.objects.all()

    if len(tasks) > 1:
        subprocess.Popen('bash run_calculations.sh', shell=True)

    return redirect('/calc_eig')
