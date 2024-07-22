"""file:main/model.
    This module is for defining the models for the main application
    class: TimeModel
        - responsible for the declaring a Time Model
 """

from django.db import models

from main.constants import TIME_ZONES_CHOICES

class TimeModel(models.Model):
    """A class for declaring the model for Time table"""
    time = models.DateTimeField()
    time_zone = models.CharField(choices=TIME_ZONES_CHOICES, default='EST', max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        A function to return the string representation of the TimeModel
        :return:
        :rtype:
        """
        return f'{self.time} {self.time_zone}'
