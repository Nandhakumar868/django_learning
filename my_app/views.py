from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mymembers = Member.objects.all()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))