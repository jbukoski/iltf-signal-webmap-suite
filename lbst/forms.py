# -*- coding: utf-8 -*-
from django import forms
from . import models

#class DocumentForm(forms.Form):
class DocumentForm(forms.ModelForm):

    """
    docfile = forms.FileField(
        label = 'Select a file',
        help_text = 'max. 400 megabytes'
    )
    """

    class Meta:
        model = models.Document
        fields = ('docfile', )
