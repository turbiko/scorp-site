from .forms import ContactForm, CareerContactForm   # Замініть на шлях до вашої форми

def contact_form(request):
    return {'contact_form': ContactForm()}


def career_contact_form(request):
    return {'career_form': CareerContactForm()}

