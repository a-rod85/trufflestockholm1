from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

    else:
        form = ContactForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(name, phone, messsage, from_email, [''])

            except BadHeaderError:
                return HttpResponse('invalid')

            return HttpResponseRedirect('contact:send_success')


    contect = {
        'form': form,
    }

    return render(request, 'contact.html', context)


def send_success(request):
    return HttpResponse('We have recieved your email, Thank you')    