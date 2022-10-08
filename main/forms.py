from django import forms

class Questions(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for obj in self.fields.values():
            obj.widget.attrs.update({'class': 'form-control'})


class Order(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    age = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for obj in self.fields.values():
            obj.widget.attrs.update({'class': 'form-control'})
