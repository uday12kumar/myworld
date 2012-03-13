from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfiles(models.Model):
    user = models.ForeignKey(User)
    udid =  models.CharField(max_length = 50)
    
    def __unicode__(self):
        return "USER : " + unicode(self.user.username)
    
    