from django.contrib.gis.db import models

    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)



#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='/uploaded')
