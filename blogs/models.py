from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    email = models.EmailField(
        verbose_name='email address',
        max_length=50,
        unique=True,)
    is_admin = models.BooleanField()
    display_name = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "is_admin", "display_name"]
    
    def __str__(self):
        return self.display_name
    
class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class TypePage(models.Model):
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Page(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    link = models.URLField()
    level = models.ForeignKey(TypePage, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    link = models.URLField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class FavoritePage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.display_name
    
class AlltopPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to="AlltopPost")
    description = models.TextField(max_length =250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title