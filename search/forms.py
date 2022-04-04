from django import forms
from .models import tickersymbol

class searchform(forms.ModelForm):
    class Meta:
        model = tickersymbol
        fields = ('ticker',)
    def __init__(self, *args, **kwargs):
        super(searchform, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
