from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
#
from .forms import PersonCreationForm
from .models import Person, Course ,Purpose,Department

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Order is placed!")
            return redirect('/schoolapp/person_add')
    return render(request, 'regform.html', {'form': form})
# #
# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})
#
#
# # AJAX
def load_course(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course.html',{'course': course})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
