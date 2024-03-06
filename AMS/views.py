from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home_view(request):
    context = {}
    return render(request, 'home-view.html', context=context)