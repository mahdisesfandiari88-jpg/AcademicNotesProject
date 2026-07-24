from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from courses.models import Course

@login_required
def note_list(request):
    notes = Note.objects.filter(course__user=request.user)

    return render(
        request,
        "notes.html",
        {
            "notes": notes,
        }
    ) 

@login_required
def course_notes(request, id):
    course = get_object_or_404(
        Course,
        id=id,
        user=request.user
    )
    notes = Note.objects.filter(
        course=course
    )
    query = request.GET.get("q")
    if query:
        notes = notes.filter(
            title__icontains=query
        )
    return render(
        request,
        "notes.html",
        {
            "course": course,
            "notes": notes,
        }
    )

@login_required
def note_create(request, id):
    course = get_object_or_404(
        Course,
        id=id,
        user=request.user
    )
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = course
            note.save()
            return redirect(
                "course_notes",
                id=course.id
            )
    else:
        form = NoteForm()
    return render(
        request,
        "add-note.html",
        {
            "form": form,
            "course": course,
        }
    )

@login_required
def note_detail(request, id):
    note = Note.objects.get(
        id=id,
        course__user=request.user
    )
    return render(
        request,
        "view-note.html",
        {
            "note": note,
        }
    )

@login_required
def note_update(request, id):
    note = Note.objects.get(
    id=id,
    course__user=request.user
    )
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(
                "course_notes",
                id=note.course.id
            )
    else:
        form = NoteForm(instance=note)
    return render(
        request,
        "add-note.html",
        {
            "form": form,
            "course": note.course,
        }
        )

@login_required
def note_delete(request, id):
    note = Note.objects.get(
        id=id,
        course__user=request.user
    )
    course_id = note.course.id
    note.delete()
    return redirect(
        "course_notes",
        id=course_id
    )