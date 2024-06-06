from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=230,
                           widget=forms.Textarea(
                               attrs={'placeholder': _('Name'), 'cols': '15', 'rows': '1', 'class': 'contact-input'}), )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': _('Email'),
            'maxlength': '235',  # Max symbols
            'class': 'contact-input'
        }))
    message = forms.CharField(label=_('Message'),
                              widget=forms.Textarea(attrs={
                                  'placeholder': _('Message'), 'cols': '15', 'rows': '1', 'class': 'contact-input'}), )


class CareerContactForm(forms.Form):
    first_name = forms.CharField(label=_('First name'),
                                 widget=forms.Textarea(attrs={
                                     'placeholder': _('First name'), 'cols': '15', 'rows': '1',
                                     'class': 'contact-input'}), )
    last_name = forms.CharField(label=_('Last name'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('Last name'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': _('Email'),
            'maxlength': '235',  # Max symbols
            'class': 'contact-input'
        }))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'contact-input','type': 'date'}))
    country_residence = forms.CharField(label=_('Country residence'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('Country residence'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    phone = forms.CharField(label=_('Phone'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('Phone'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    nationality = forms.CharField(label=_('nationality'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('nationality'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    main_skill = forms.CharField(label=_('Main skill'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('Main skill'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    secondary_skill = forms.CharField(label=_('secondary skill'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('secondary skill'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    other_skill = forms.CharField(label=_('other skill'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('other skill'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    software = forms.CharField(label=_('software'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('software'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    availability = forms.CharField(label=_('availability'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('availability'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    linkedin = forms.CharField(label=_('linkedin'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('linkedin'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    website_reel = forms.CharField(label=_('website/reel'),
                                widget=forms.Textarea(attrs={
                                    'placeholder': _('website/reel'), 'cols': '15', 'rows': '1',
                                    'class': 'contact-input'}), )
    message_about = forms.CharField(label=_('Message'),
                                    widget=forms.Textarea(attrs={
                                        'placeholder': _('Message'),
                                        'cols': '15', 'rows': '1', 'class': 'contact-input'}), )

