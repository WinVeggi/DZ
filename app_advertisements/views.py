from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advertisements
from .forms import AdvertisementsForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# def index(request):
#     advertisemenets=Advertisements.objects.all()
#     context = {'advertisements': advertisemenets}
#     return render(request, 'advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'advertisements/top-sellers.html')
@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementsForm()
    context = {'form':form}
    return render(request, 'advertisements/advertisement-post.html', context)

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisements.objects.filter(title=title)
    else:
        advertisements = Advertisements.objects.all()
    contex = {'advertisements':advertisements}
    return render(request, 'app_advertisements/index.html', contex)