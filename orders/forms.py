from django import forms
from .models import Product

class orderingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items')
        super(orderingForm, self).__init__(*args, **kwargs)
        for item in items:
            self.fields[item.name] = forms.IntegerField(label=item.image.url, required=False)
