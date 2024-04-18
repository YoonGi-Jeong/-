from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        #exclude = ("created_at","updated_at")







    #GENRE_CHOICES =[
        #("Buy","삽니다"),
        #("Sell", "팝니다"),
        #("Show off","자랑하기"),
    #]

    #genre = forms.ChoiceField(choices=GENRE_CHOICES)