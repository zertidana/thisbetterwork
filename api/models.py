from turtle import title
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    def __str__(self):
        """Return the title of the category."""
        return self.title
        
    class Meta:
        verbose_name_plural='Categories'

class News(models.Model):
    """ 
    A Category has many news articles within it, so the 
    foreign key below describes a many to one relationship
    Also that, once the category is deleted, all related artciles are also deleted
    """
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return self.title