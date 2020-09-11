from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def about_us(request):
    return render(request, 'about_us.html', context={})

def contacts(request):
    return render(request, 'contacts.html', context={})

def legitimacy_activities(request):
    return render(request, 'legitimacy_activities.html', context={})

def download_catalog(request):
    return render(request, 'download_catalog.html', context={})

def news(request):
    return render(request, 'in_development.html', context={})
