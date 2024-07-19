"""file: main/views.py
    This module contains the main views of the main application.
"""

from django.shortcuts import render

from .forms import TimeModelForm

def index(request):
    """
    This is the main view of the main application.
    :param request:
    :type request:
    :return:
    :rtype:
    """
    if request.method == 'POST':
        form = TimeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TimeModelForm()
    return render(request, 'main/index.html', {"form": form})
