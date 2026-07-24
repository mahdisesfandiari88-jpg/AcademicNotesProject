from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .models import File
from .forms import FileForm
from courses.models import Course


@login_required
def course_files(request, id):
    course = get_object_or_404(
        Course,
        id=id,
        user=request.user
    )
    files = File.objects.filter(
        course=course
    )
    query = request.GET.get("q")
    if query:
        files = files.filter(
            title__icontains=query
        )
    return render(
        request,
        "files.html",
        {
            "course": course,
            "files": files,
        }
    )

@login_required
def file_create(request, id):
    course = get_object_or_404(
        Course,
        id=id,
        user=request.user
    )
    if request.method == "POST":
        form = FileForm(
            request.POST,
            request.FILES
        )
        print(form.errors)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.course = course
            uploaded_file.save()
            return redirect(
                "course_files",
                id=course.id
            )
    else:
        form = FileForm(
            initial={
                "course": course
            }
        )
    return render(
        request,
        "upload-file.html",
        {
            "form": form,
            "course": course,
        }
    )
@login_required
def file_delete(request, id):

    file = get_object_or_404(
        File,
        id=id,
        course__user=request.user
    )

    course_id = file.course.id

    if request.method == "POST":
        file.delete()

    return redirect("course_files", id=course_id)