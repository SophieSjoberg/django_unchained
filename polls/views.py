from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse('Tjena mittbena!')



def whatever(request):
  return HttpResponse('Shuu Tjejen!!')
