from django import forms
from .models import Product

class orderingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items')
        super(orderingForm, self).__init__(*args, **kwargs)
        counter = 1
        for item in items:
            self.fields['question-' + str(counter)] = forms.IntegerField(label=item.image.url)
            counter += 1
