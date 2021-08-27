from django.http import HttpResponse
from django.shortcuts import render
from .models import Tuz, City
from requests import get
from json import loads

def tuzy_lista(request):
    # tuzy = Tuz.objects.all().order_by('date')
    # return render(request, 'tuzy/tuzy_lista.html', {'tuzy': tuzy})


    results=City.objects.all().order_by('id')
    
    if request.POST:
        val = request.POST["city"]
        miasto="dupa"
        if val == '1':
            miasto = "Warszawa"
        elif val == '2':
            miasto = "Lublin"
        elif val == '3':
            miasto = "Katowice"
        elif val == '4':
            miasto = "Szczecin"

        print(f"val={val}")
        print(miasto)
        url = 'https://danepubliczne.imgw.pl/api/data/synop'
        response = get(url)
        for row in loads(response.text):
            if row['stacja'] == miasto:
                print(row)
                return render(request, 'tuzy/tuzy_lista.html',{"showcity":results, "stacja":row})
    return render(request, 'tuzy/tuzy_lista.html',{"showcity":results})


# def tuz(request, slug):
#     return HttpResponse(slug)

def tuz(request, slug):
    #return HttpResponse(slug)
    tuz = Tuz.objects.get(slug=slug)
    return render(request,'tuzy/tuz.html',{'tuz': tuz})

