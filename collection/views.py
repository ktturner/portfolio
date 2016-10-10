from django.shortcuts import render
from collection.models import Pattern
from collection.models import Illustration
from collection.models import Sketchbook
from collection.models import UploadPattern
from collection.models import UploadIllustration
from collection.models import UploadSketchbook
from collection.forms import ContactForm

def index(request):
    return render(request, 'index.html')

def pattern(request):
    patterns = Pattern.objects.all()
    uploads_patterns = UploadPattern.objects.all()
    return render(request, 'pattern.html', {'patterns' : patterns, 'uploads_patterns': uploads_patterns, })

def illustration(request):
    illustrations = Illustration.objects.all()
    uploads_illustrations = UploadIllustration.objects.all()
    return render(request, 'illustration.html', {'illustrations' : illustrations, 'uploads_illustrations': uploads_illustrations, })

def sketchbook(request):
    sketchbooks = Sketchbook.objects.all()
    uploads_sketchbooks = UploadSketchbook.objects.all()
    return render(request, 'sketchbook.html', {'sketchbooks' : sketchbooks, 'uploads_sketchbooks': uploads_sketchbooks,})

def pattern_detail(request, slug):
    pattern = Pattern.objects.get(slug=slug)
    return render(request, 'patterns/pattern_detail.html', {'pattern':pattern,})

def illustration_detail(request, slug):
    illustration = Illustration.objects.get(slug=slug)
    return render(request, 'illustrations/illustration_detail.html', {'illustration': illustration,})

def sketchbook_detail(request, slug):
    sketchbook = Sketchbook.objects.get(slug=slug)
    return render(request, 'sketchbooks/sketchbook_detail.html', {'sketchbook':sketchbook,})

def contact(request):
    print "inside contact"
    form_class = ContactForm
    print "adding contact views"
    return render(request, 'contact.html', {'form': form_class,})
