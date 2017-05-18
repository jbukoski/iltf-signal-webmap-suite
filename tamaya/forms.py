# -*- coding: utf-8 -*-
from django import forms
from .models import Document

#class DocumentForm(forms.Form):
class DocumentForm(forms.ModelForm):

    """
    docfile = forms.FileField(
        label = 'Select a file',
        help_text = 'max. 400 megabytes'
    )
    """

    class Meta:
        model = Document
        fields = ('docfile', )
