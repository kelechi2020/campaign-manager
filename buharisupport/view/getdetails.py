import json
import mimetypes

from django.core.serializers import json
from django.http.response import HttpResponse, JsonResponse

from buharisupport.models import State


def getdetails (request):
    #country_name = request.POST['country_name']
    country_name = request.GET['cnt']

    print ("ajax country_name ", country_name)

    result_set = []
    all_lga = []

    answer = str(country_name[1:-1])
    selected_state = State.objects.get(name=country_name)
    print ("selected state name ", selected_state)

    all_lga = selected_state.localgovernment_set.all()
    for lga in all_lga:
        print ("city name", lga.name)

        result_set.append({'name': lga.name})

    return JsonResponse (result_set, safe=False)
    # return HttpResponse(json.dump(result_set), mimetypes='application/json', content_type='application/json')
