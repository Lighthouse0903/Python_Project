from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import registrationForm

# Create your views here.
def index(request):
    return render(request, "pages/home.html")
def register(request):
    form = registrationForm()
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'pages/register.html', {'form': form})