from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from details.models import DetailModel
from user.models import UserModel
from datetime import datetime
from django.contrib.gis.geos import Point


def details(request):
    return render(request, "details.html")


def index(request):
    return render(request, 'index.html')


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


def test(request):
    on_map_objects = DetailModel.objects.all()
    pass
