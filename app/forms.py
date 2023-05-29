from django import forms
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=30, label='タイトル')
#     content = forms.CharField(label='内容', widget=forms.Textarea())


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "content", "image")
        labels = {
            "title": "タイトル",
            "content": "内容",
            "image": "画像",
        }

        error_messages = {
            "title": {
                "required": "タイトルが入力されていません",
            }
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        a = self.fields
        for i in self.fields.values():
            i.widget.attrs["class"] = "form-control mb-3 "