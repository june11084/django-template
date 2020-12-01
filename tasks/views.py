from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Todo


# Create your views here.

# this view renders some predefined tasks

def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def add(request):
    # determine if the user is submitting a task via the form or just viewing the add task page
    # if the user is just viewing the add task page, else statement will render add.html page
    if request.method == 'POST':
        # get the entered task from the request
        task = request.POST.get('task')
        # add the task to the todo table
        Todo.objects.create(task=task)  # task on the left is column name in the table
        # render the index page with the updated list of tasks
        return redirect('index')
    else:
        return render(request, 'tasks/add.html')


def contact(request):
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return render(request, 'tasks/thanks.html')
        else:
            form = ContactForm()
            context = {'form': form, 'error': 'Data is not valid!'}
            return render(request, 'tasks/contact.html', context)
    else:
        # if this a GET, we'll create a blank form
        form = ContactForm()
        context = {'form': form}
        return render(request, 'tasks/contact.html', context)
