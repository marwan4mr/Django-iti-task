from django.shortcuts import redirect, render
from django.http import HttpResponse
from random import random


my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Movie-1',
        'priority': 1,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Movie-2',
        'priority': 4,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj ",
    },
    {
        'index': 2,
        'id': 4,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj ",
    },
    {
        'index': 2,
        'id': 5,
        'name': 'Movie-5',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj ",
    },
    {
        'index': 2,
        'id': 6,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam ",
    },
]

def _get_target_task(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    # Getting index of the required task from my_task_list
    if len(final_list) == 0:
        return -1
    else:
        index_of_task = my_task_list.index(final_list[0])
        return index_of_task

# Create your views here.
def index(request):

    return render(request, 'todo/task_list.html', context={"my_task_list": my_task_list})

def create_task_dict(p):
    return  {
    'index': p.get('index') or len(my_task_list),
    'id':  int(p.get('id') or random()*10000),
    'name': p.get('task_name'),
    'priority': p.get('priority'),
    'description': p.get('description')
    }

def tasks(request, **kwargs):
    # kwargs have task id
    t = _get_target_task(kwargs.get('task_id'))
    if t == -1:
        return HttpResponse("404 man, there is no task with that id")
    # create in task/id doesn't make anysense
    if request.method == 'POST':
        p = request.POST
        if p.get('op') == 'DELETE':

            my_task_list.pop(t)
            return redirect('todo:index')

        elif p.get('op') == 'UPDATE':
            print("\n\n------it wants to update------\n\n")
            print(p)
            # be careful of unpacking request.post it's not a simple dectianory     
            updated_task = create_task_dict(p)
            print(updated_task)
            my_task_list[t] = updated_task
            return redirect('todo:index')
    elif request.method == 'GET':
        return render(request, 'todo/task.html', context=my_task_list[t])

    # return render(request, 'task.html', context={
    #     'index': 2,
    #     'id': 3,
    #     'name': 'Movie-3',
    #     'priority': 2,
    #     'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    # })

def create_task(request):
    if request.method == 'POST':
        p = request.POST
        new_task = create_task_dict(p)
        my_task_list.append(new_task)
        return redirect('todo:index')
    elif request.method == 'GET':
        return render(request, 'todo/task_create.html')
    
def update_task(request, **kwargs):
    t = _get_target_task(kwargs.get('task_id'))
    if t == -1:
        return HttpResponse("404 man, there is no task with that id")
    return render(request, 'todo/task_update.html', context=my_task_list[t])