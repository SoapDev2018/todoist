from django.shortcuts import render, get_object_or_404, redirect

from .models import Todo
from .forms import TodoModelForm

# Create your views here.
def todo_list_view(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TodoModelForm()
    object_list = Todo.objects.all()
    template_name = 'todo/list.html'
    context = {
        "title": "All Todos",
        "form": form,
        "object_list": object_list,
    }
    return render(request, template_name, context=context)

def todo_update_view(request, slug):
    obj = get_object_or_404(Todo, slug=slug)
    form = TodoModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = TodoModelForm()
        return redirect('/todos/')
    template_name = 'todo/edit.html'
    context = {
        "title": "Edit Todo",
        "form": form,
        "obj": obj,
    }
    return render(request, template_name, context=context)