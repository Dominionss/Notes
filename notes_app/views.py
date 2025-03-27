from django.shortcuts import render, HttpResponse
from .models import Note


def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def create_note(request):
    return render(request, 'create.html')
