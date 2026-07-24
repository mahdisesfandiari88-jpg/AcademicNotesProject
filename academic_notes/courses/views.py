from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from notes.models import Note
from files.models import File

@login_required
def dashboard(request):
    courses = Course.objects.filter(
        user=request.user
    )
    recent_files = File.objects.filter(
        course__user=request.user
    ).order_by("-uploaded_at")[:5]

    recent_notes = Note.objects.filter(
        course__user=request.user
    ).order_by("-created_at")[:5]

    message = None
    query = request.GET.get("q")
    if query:
        course = courses.filter(
            name__icontains=query
        ).first()
        if course:
            return redirect(
                "course_detail",
                id=course.id
            )
        else:
            message = "Course not found."
            print("RECENT FILES:", recent_files)
    return render(
        request,
        "dashboard.html",
        {
            "courses": courses,
            "recent_files": recent_files,
            "recent_notes": recent_notes,
            "message": message,
        }
    )

@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()

            return redirect("course_detail", id=course.id)
    else:
        form = CourseForm()
    return render(request, "add-course.html", {"form": form})

@login_required
def course_detail(request, id):
    course = Course.objects.get(
        id=id,
        user=request.user
    )
    notes = course.note_set.all()
    notes_count = notes.count()

    files = course.file_set.all()

    files_count = files.count()
    recent_files = files.order_by(
        "-uploaded_at"
    )[:3]
    return render(
        request,
        "course-details.html",
        {
            "course": course,
            "notes": notes,
            "notes_count": notes_count,
            "files": files,
            "files_count": files_count,
            "recent_files": recent_files,
        },
    )

@login_required
def course_update(request, id):
    course = Course.objects.get(id=id, user=request.user)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_detail", id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, "edit-course.html", {
        "form": form,
        "course": course,
    })


@login_required
def course_delete(request, id):
    course = Course.objects.get(id=id, user=request.user)
    course.delete()
    return redirect("dashboard")