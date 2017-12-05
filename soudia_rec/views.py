from django.shortcuts import render
from django.views.generic import ListView
from .models import Employer, Candidate, We_work

# Create your views here.

# def index(request):
#     employer = Employer.objects.all()
#     context = {
#         'employer' : employer,
#     }
#     return render(request, "index.html", context)

class IndexView(ListView):
    context_object_name = 'home_list'
    template_name = 'index.html'
    queryset = Employer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['employer'] = Employer.objects.all()
        context['candidate'] = Candidate.objects.all()
        context['client'] = We_work.objects.all()
        # And so on for more models
        return context


def find_a_job(request):
    context = {}
    return render(request, "find-a-job.html", context) 

def cart(request):
    context = {}
    return render(request, "cart-2.html", context) 


def post_a_job(request):
    context = {}
    return render(request, "post-a-job.html", context) 

def how_it_works(request):
    context = {}
    return render(request, "how-it-works.html", context)  
