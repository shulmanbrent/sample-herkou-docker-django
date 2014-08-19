from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.cache import cache
import sys

def home(request):
  return render_to_response('index.html', {})

def command(request):
  try:
    a = request.GET["a"]
    if a == 'set':
      res = cache._cache.set('welcome_msg', 'Hello from Redis!')
    elif a =='get':
      res = cache._cache.get('welcome_msg')
    elif a == 'stats':
      res = ''.join(['%s: %s<br/>' % (k,v) for k,v in cache._cache.stats().iteritems()])      
    elif a == 'delete':
      res = cache._cache.delete('welcome_msg')
    else:
      res = ''
  except Exception as e:
    print "Error: %s" % e 
    return HttpResponse("Error")

  return HttpResponse(str(res))
