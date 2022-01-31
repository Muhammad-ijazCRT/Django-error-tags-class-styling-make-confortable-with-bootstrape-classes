# send message to index.html


from django.contrib import messages
messages.add_message(request, messages.INFO, 'Hello world.')