from django.shortcuts import render, HttpResponse, redirect
from .models import Note
from .forms import NoteForm


def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NoteForm()
    return render(request, "create.html", {"form": form})
