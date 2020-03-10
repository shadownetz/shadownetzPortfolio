from django import forms


class NewContentForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Blog Title'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control wysiwyg-editor', 'placeholder': 'Blog Content'
    }))
    tags = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': "Blog tags (separate with commas)"
    }), required=False)
    display_image = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': "Blog Display Image (URL)"
    }), required=False)
