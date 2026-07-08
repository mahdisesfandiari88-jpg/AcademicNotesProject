from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.contrib.auth.models import User
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    text = "Course List:\n"
    for course in courses:
        text += course.name + "\n"
    return HttpResponse(text)


def course_create(request):
    form = CourseForm(request.POST)
    if form.is_valid():
        course = form.save(commit=False)
        course.user = User.objects.first()
        course.save()
        return HttpResponse("Course Created")
    else:
        form = CourseForm()
        return render(request, "course_create.html", {"form": form})
    
def course_detail(request, id):
    course = Course.objects.get(id=id)
    return HttpResponse(course.name)

def course_update(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponse("Course Updated")
    else:
        form = CourseForm(instance=course)
    return render(request, "course_create.html", {"form": form})

def course_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return HttpResponse("Course Deleted")