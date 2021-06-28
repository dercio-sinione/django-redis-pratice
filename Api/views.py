from django.shortcuts import render
from django.http import JsonResponse

from .models import Friends, Users
from .utils import Redis
from django.db.models.functions import Cast
from django.db.models import CharField, TextField
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
import time
  # return render(request, 'Web/render.html', {"obj": obj} )
  # return JsonResponse(obj, safe=False)

def friends_redis(request):
  cache_data = Redis.get(Friends.__name__)
  if cache_data:
    return render(request, 'Api/render.html', {"obj": cache_data})
  return render(request, 'Api/render.html', {"obj": cache_data})


def friends(request):
  obj = list(Friends.objects.select_related().values())
  # print(obj[0])
  Redis.set(Friends.__name__, obj)
  # friends = list()
  # for item in obj:
  #   owner = Users.objects.get(pk=item['owner_id'])
  #   friends.append(Friends(id=item['id'], name=item['name'], age=item['age'], email=item['email'], owner=owner, creation_date=item['creation_date']))
  
  start_time = time.time()
  obj = [Friends(id=item['id'], name=item['name'], age=item['age'], email=item['email'], owner=Users.objects.get(pk=item['owner_id']), creation_date=item['creation_date'])
               for item in obj]
  end_time = time.time()
  print(f'it take {(end_time-start_time):.4f}s')
  return render(request, 'Api/render.html', {"obj": obj})
