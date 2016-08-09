from django.shortcuts import render
from collection.models import Pattern
from collection.models import Illustration
from collection.models import Sketchbook

def index(request):
    return render(request, 'index.html')

def pattern(request):
    patterns = Pattern.objects.all()
    return render(request, 'pattern.html', {'patterns' : patterns,})

def illustration(request):
    illustrations = Illustration.objects.all()
    return render(request, 'illustration.html', {'illustrations' : illustrations,})

def sketchbook(request):
    sketchbooks = Sketchbook.objects.all()
    return render(request, 'sketchbook.html', {'sketchbooks' : sketchbooks,})

def pattern_detail(request, slug):
    pattern = Pattern.objects.get(slug=slug)
    return render(request, 'patterns/pattern_detail.html', {'pattern':pattern,})

def illustration_detail(request, slug):
    illustration = Illustration.objects.get(slug=slug)
    return render(request, 'illustrations/illustration_detail.html', {'illustration': illustration,})

def sketchbook_detail(request, slug):
    sketchbook = Sketchbook.objects.get(slug=slug)
    return render(request, 'sketchbooks/sketchbook_detail.html', {'sketchbook':sketchbook,})
