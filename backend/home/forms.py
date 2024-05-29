from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=230,
                           widget=forms.Textarea(attrs={'placeholder': _('Name'), 'cols': '15', 'rows': '1'}), )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': _('Email'),
            'maxlength': '235',  # Max symbols
        }))
    message = forms.CharField(label=_('Message'),
                              widget=forms.Textarea(attrs={
                                  'placeholder': _('Message'), 'cols': '15', 'rows': '1'}), )
