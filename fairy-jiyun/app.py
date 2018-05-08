import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from django_micro import configure, route, run
from django.shortcuts import redirect, render
from forms import VerifyForm
import cognitive_face as CF

DEBUG = True

CF.Key.set('422e22b5703d44c0a0dc19c35fd51c9f')
CF.BaseUrl.set('https://eastus.api.cognitive.microsoft.com/face/v1.0')

configure(locals())


@route('', name='index')
def index(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST, request.FILES)
        if form.is_valid():
            form.verify()
    else:
        form = VerifyForm()

    return render(request, 'index.html', {'form': form})


application = run()

