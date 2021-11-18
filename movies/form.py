from django.forms import ModelForm
from . import models

class MovieForm(ModelForm):
    # DRY it's already written in model.py why rewrite it here
    # name = forms.CharField(max_length=250, label="movie name")
    class Meta:
        model = models.Movie
        # fields = ['name',]
        # if you want all fields look no further than __all__
        fields = '__all__'

