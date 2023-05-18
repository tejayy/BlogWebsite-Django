from django import forms
from .models import Post


'''POST FORM'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title here...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title_tag here...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your blog_content here...'}),
        }
        
'''Edit POST Form'''
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title here...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title_tag here...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Blog Content here...'}),
        }