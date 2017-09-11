from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render

from . import forms


def index(request):
    return render(request, 'personal/home.html')


def contact(request):

    if request.method == 'GET':
        form = forms.ContactForm()
        return render(request, 'personal/basic.html', {'form': form})

    elif request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():

            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            contact_message = form.cleaned_data['message']

            template =  get_template('personal/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
            }
            content = template.render(context)

            from_email = settings.DEFAULT_FROM_EMAIL

            send_mail(
                'New message from Contact form', 
                content, 
                'Contact <{}>'.format(from_email), 
                ['blabla@bla.com'] 
            )

            messages.add_message(request, messages.SUCCESS, 'Thanks for contacting us!')

            return HttpResponseRedirect(reverse('contact'))


