from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    category = models.CharField(max_length=50,blank=True)
    summary = models.CharField(max_length=100,blank=True)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
    def get_absolute_url(self):
        path = reverse('ruiblog:detail',args=(self.id,))
        print('the path is %s'%path) 
        return "http://127.0.0.1/ruiblog/%s"%path

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if self.summary=='' or self.summary == None:
            summaryTemp = self.body.__str__()[0:100]
            self.summary = summaryTemp
        super(BlogsPost,self).save(*args,**kwargs)
        

class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','timestamp')
    
admin.site.register(BlogsPost,BlogPostAdmin)
