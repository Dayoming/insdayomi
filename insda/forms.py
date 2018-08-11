from django.forms import ModelForm
from insda.models import Article


class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'photo', 'contents']