from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobbies, Portfolio
from django.template import loader
from .forms import ContactForm
from .forms import PortfolioForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):

    template = loader.get_template('portfolio/home.html')
    return render(request, 'portfolio/home.html')


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    template = loader.get_template('portfolio/hobbies.html')
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'portfolio/hobbies.html', context)


def hobby_detail(request, hobby_id):
    hobby = Hobbies.objects.get(pk=hobby_id)
    template = loader.get_template('portfolio/hobby_detail.html')
    context = {
        'hobby': hobby,
    }
    return render(request, 'portfolio/hobby_detail.html', context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    template = loader.get_template('portfolio/portfolio.html')
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'portfolio/portfolio.html', context)


def portfolio_detail(request, project_id):
    project = Portfolio.objects.get(pk=project_id)
    template = loader.get_template('portfolio/portfolio_detail.html')
    context = {
        'project': project,
    }
    return render(request, 'portfolio/portfolio_detail.html', context)


def contact(request):

    template = loader.get_template('portfolio/contact.html')
    return render(request, 'portfolio/contact.html')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact_form.html', {'form': form})

@login_required
def portfolio_form(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

@login_required
def update_portfolio(request, id):
    project = Portfolio.objects.get(id=id)
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'portfolio/portfolio_form.html', {'form': form, 'portfolio': project})

@login_required
def delete_portfolio(request, id):
    project = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        project.delete()
        return redirect('home')

    return render(request, 'portfolio/portfolio_delete.html', {'portfolio': project})



