from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from details.models import DetailModel
from user.models import UserModel
from datetime import datetime
from django.contrib.gis.geos import Point
import json


def details(request):
    if request.user.is_authenticated:
        return render(request, "details.html")
    else:
        return redirect('user:login')


def save_details(request):
    if request.method == "POST":
        user = UserModel.objects.get(pk=request.user.pk)
        try:
            settings = DetailModel.objects.create(
                user=user,
                title=request.POST['title'],
                image=request.FILES['image'],
                description=request.POST['description'],
                classification=request.POST['classification'],
                point=Point(float(request.POST['longitude']), float(request.POST['latitude'])),
                author=request.user.first_name,
                date=datetime.now()
            )
            settings.save()
            return JsonResponse({"added": "added"})
        except Exception as e:
            print(e)
            return JsonResponse({"not added": "not added"})
    else:
        return HttpResponseForbidden()


def index(request):
    on_map_objects = DetailModel.objects.all()
    objs = {}
    photo = ''
    for i, obj in enumerate(on_map_objects):
        objs[i] = {"email": obj.user.email, "title": obj.title,
                   "classification": obj.classification, "description": obj.description, "coords": obj.point.coords,
                   "photo": obj.image.url}
        photo = obj.image.url
    return render(request, 'index.html', {'map_objs': json.dumps(objs), "photo": photo,
                                          "watermark": "static/images/200-star.jpg"})
