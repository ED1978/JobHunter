from django.shortcuts import render
from django.http import HttpResponse
from jobsearch.models import *

def index(request):

    load_data()

    jobs = Job.objects.all()

    return render(request, "jobsearch/index.html", locals())

# Create your views here.
