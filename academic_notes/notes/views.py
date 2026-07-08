from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm


def note_list(request):
    notes = Note.objects.all()
    text = "Note List:\n"
    for note in notes:
        text += note.title + "\n"
    return HttpResponse(text)

from .forms import NoteForm


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Note Created")
    else:
        form = NoteForm()
    return render(request, "note_create.html", {"form": form})

def note_detail(request, id):
    note = Note.objects.get(id=id)
    text = f"""
    Title: {note.title}
    Description:
    {note.description}
    Content:
    {note.content}
    """
    return HttpResponse(text)

def note_update(request, id):
    note = Note.objects.get(id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponse("Note Updated")
    else:
        form = NoteForm(instance=note)
    return render(request, "note_create.html", {"form": form})

def note_delete(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return HttpResponse("Note Deleted")