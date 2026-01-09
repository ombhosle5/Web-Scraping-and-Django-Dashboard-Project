from django.db import models



class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    tags = models.CharField(max_length=500)
    author_profile = models.URLField(max_length=500)
    
    class Meta:
        db_table = 'quotes'   
        managed = False   
    
    def __str__(self):
        return f"{self.quote[:50]}... - {self.author}"