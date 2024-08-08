"""file: main/forms.py
    This module if for making forms from django model
    class: TimeModelForm
        - responsible for making form from TimeModel
"""

from django.forms import ModelForm

from main.models import TimeModel


class TimeModelForm(ModelForm):
    """A class to make form for Time Model """
    class Meta:
        """A class to make form for Time Model"""
        model = TimeModel
        fields = ["time", "time_zone"]
