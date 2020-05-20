from django.shortcuts import render

from .models import Todo
from .forms import TodoModelForm

# Create your views here.
def todo_list_view(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TodoModelForm()
    object_list = Todo.objects.all()
    template_name = 'blogs/list.html'
    context = {
        "title": "All Todos",
        "form": form,
        "object_list": object_list,
    }
    return render(request, template_name, context=context)