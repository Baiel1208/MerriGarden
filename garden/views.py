from django.shortcuts import render, redirect
from . import models as m

# Create your views here.
def index(request):
    order = m.Order.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')
        m.Order.objects.create(name=name, phone_number=phone_number, date=date)
        return redirect('index')

    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())

def team(request):
    return render(request, 'team.html', locals())