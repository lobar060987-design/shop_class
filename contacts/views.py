from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

from contacts.forms import ContactModelForm
from contacts.models import ContactModel


def contact_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('contacts:contact')

    else:
        form = ContactModelForm()

        context = {'form': form}

        return render(request, 'contact.html', context)

