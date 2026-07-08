from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required

@login_required
def course_list(request):
    courses = Course.objects.filter(user=request.user)
    text = "Course List:\n"
    for course in courses:
        text += course.name + "\n"
    return HttpResponse(text)

@login_required
def course_create(request):
    form = CourseForm(request.POST)
    if form.is_valid():
        course = form.save(commit=False)
        course.user = request.user
        course.save()
        return HttpResponse("Course Created")
    else:
        form = CourseForm()
        return render(request, "course_create.html", {"form": form})
    
@login_required
def course_detail(request, id):
    course = Course.objects.get(id=id, user=request.user)
    return HttpResponse(course.name)

@login_required
def course_update(request, id):
    course = Course.objects.get(id=id, user=request.user)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponse("Course Updated")
    else:
        form = CourseForm(instance=course)
    return render(request, "course_create.html", {"form": form})

@login_required
def course_delete(request, id):
    course = Course.objects.get(id=id, user=request.user)
    course.delete()
    return HttpResponse("Course Deleted")

