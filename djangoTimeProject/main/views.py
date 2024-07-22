"""file: main/views.py
    This module contains the main views of the main application.
"""

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from main.forms import TimeModelForm

class TimeModelFormView(FormView):
    """
    Class-based view to handle TimeModelForm submission.
    """
    form_class = TimeModelForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        A function to check if the form is valid, save the form and redirect to the success URL.
        args:
        - form: The form to be validated
        return:
        - redirects to the success URL
        """
        form.save()
        return super().form_valid(form)
