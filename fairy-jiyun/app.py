import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from django_micro import configure, route, run
from django.shortcuts import redirect, render
from forms import VerifyForm
import cognitive_face as CF

DEBUG = True
SUBSCRIPTION_KEY = os.environ.get('SUBSCRIPTION_KEY')
COGNITIVE_FACE_REGION = os.environ.get('COGNITIVE_FACE_REGION', 'eastasia')

CF.Key.set(SUBSCRIPTION_KEY)
CF.BaseUrl.set('https://{}.api.cognitive.microsoft.com/face/v1.0/'.format(COGNITIVE_FACE_REGION))

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

