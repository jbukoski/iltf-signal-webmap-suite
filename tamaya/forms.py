# -*- coding: utf-8 -*-
from django import forms
from django.db import models

class DocumentForm(forms.Form):

    print("\nWe are in DocumentForm...")
    print("forms: ", forms)
    print("\n")

    docfile = forms.FileField(
        label = 'Select a file',
        help_text = 'max. 400 megabytes'
    )

###########################
## For file upload
###########################

class Document(models.Model):
    #docfile = models.FileField(upload_to='documents/')
    docfile = models.FileField(upload_to='tamaya/sample_up')
