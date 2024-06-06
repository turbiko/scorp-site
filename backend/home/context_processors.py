from .forms import ContactForm, CareerContactForm   # Замініть на шлях до вашої форми

def contact_form(request):
    return {'form': ContactForm()}


def career_contact_form(request):
    return {'form': CareerContactForm()}

