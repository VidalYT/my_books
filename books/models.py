from django.db import models

# New seccion of the code added (To get All URL Generated).
class Category(models.Model):
    title = models.CharField(max_length=250) 

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)  
    author = models.CharField(max_length=250)  
    image = models.CharField(max_length=2000) 
    created_at =models.CharField(auto_now_add=True) 
    update_at = models.CharField(auto_now=True) 

