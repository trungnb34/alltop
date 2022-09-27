from django.contrib import admin
from .models import Page, Post, FavoritePage, AlltopPost, Category, TypePage

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    # prepopulated_fields = ("link",)
    list_display = ("title", "link")
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "link")
    
@admin.register(TypePage)
class TypePageAdmin(admin.ModelAdmin):
    list_display = ("title",)