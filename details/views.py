from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from details.models import DetailModel
from user.models import UserModel
from datetime import datetime
from django.contrib.gis.geos import Point
from cloudinary import CloudinaryImage


def details(request):
    return render(request, "details.html")


def index(request):
    return render(request, 'index.html')


def save_details(request):
    if request.method == "POST":
        user = UserModel.objects.get(pk=request.user.pk)
        photo = request.FILES['image']
        image = CloudinaryImage(photo).image(
            overlay="static/images/200-star.jpg"
        )
        try:
            settings = DetailModel.objects.create(
                user=user,
                title=request.POST['title'],
                image=image,
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
