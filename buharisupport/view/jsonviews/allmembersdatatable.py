from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from buharisupport.models import Members


def peopleajax(request):
    table = Members.objects.all()
    #ata = serializers.serialize("json", Members.objects.all())
    #data = json.loads(ata)
    data = list(table.values())
    #from pprint import pprint
    #pprint(data)
    return JsonResponse({'data':data})
    #return HttpResponse(data, content_type='application/json')


def peopleview(request):

    return render(request, 'datatables/allmembers.html')