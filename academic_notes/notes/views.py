from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

@login_required
def note_list(request):
    notes = Note.objects.filter(course__user=request.user)
    text = "Note List:\n"
    for note in notes:
        text += note.title + "\n"
    return HttpResponse(text)

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if note.course.user != request.user:
                return HttpResponse("You cannot add note to this course")
            note.save()
            return HttpResponse("Note Created")
    else:
        form = NoteForm()
    return render(request, "note_create.html", {"form": form})

@login_required
def note_detail(request, id):
    note = Note.objects.get(
    id=id,
    course__user=request.user
    )
    text = f"""
    Title: {note.title}
    Description:
    {note.description}
    Content:
    {note.content}
    """
    return HttpResponse(text)

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
            return HttpResponse("Note Updated")
    else:
        form = NoteForm(instance=note)
    return render(request, "note_create.html", {"form": form})

@login_required
def note_delete(request, id):
    note = Note.objects.get(
    id=id,
    course__user=request.user
    )
    note.delete()
    return HttpResponse("Note Deleted")