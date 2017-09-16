# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserMessage
import MySQLdb

# Create your views here.

def getform(request):
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print message.name

    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.email = email
        user_message.save()
    # message = None
    # all_messages = UserMessage.objects.all()
    # if all_messages:
    #     message = all_messages[0]
    return render(request, 'message_form.html', {
        # "my_message": message
    })