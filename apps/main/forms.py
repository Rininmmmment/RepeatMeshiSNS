from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["user"]
        fields = ['image', 
                  'food_name', 
                  'restaurant_name', 
                  'place', 
                  'price',
                  'review', 
                  'free_text']

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        article = super().save(commit=False)
        if self.user:
            article.user = self.user
        if commit:
            article.save()
        return article