from django import forms
from blog.models import Blog, Category, Tag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'tags',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('label',)
