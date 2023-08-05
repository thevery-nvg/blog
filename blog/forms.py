from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget, label='Текст')

    class Meta:
        model = Post
        fields = '__all__'


class AddPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget, label='Текст')

    class Meta:
        model = Post
        exclude = ['views', 'slug', 'author']
