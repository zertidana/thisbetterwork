from turtle import title
from django.db import models
from multiselectfield import MultiSelectField

# Categories
class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    def __str__(self):
        """Return the title of the category."""
        return self.title

    class Meta:
        verbose_name_plural='Categories'

# News Articles
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

# Comments
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE) 
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    image=models.ImageField(upload_to='imgs/')
    comment=models.TextField()
    add_time=models.TimeField(auto_now_add=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment
    
class Profile(models.Model):
    ProfileImage = models.ImageField(upload_to='imgs/')
    Email = models.EmailField(max_length=254)
    DoB = models.DateField()
    CAT_CHOICES = (('SPORTS', 'Sports'),
              ('FASHION', 'Fashion'),
              ('EDUCATION', 'Education'),
              ('ART', 'Art'),
              ('WORLDNEWS', 'World News'),
              ('FINANCE', 'Finance'))
    Favourite = MultiSelectField(choices=CAT_CHOICES,max_choices=9,max_length=9)