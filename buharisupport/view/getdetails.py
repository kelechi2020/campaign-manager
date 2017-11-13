from django.http.response import HttpResponse, JsonResponse
from buharisupport.models import State, LocalGovernment, Ward


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


def get_ward(request):
    # country_name = request.POST['country_name']
    country_name = request.GET['cnt']

    print("ajax country_name ", country_name)

    result_set = []
    all_lga = []

    answer = str(country_name[1:-1])
    selected_localgov = LocalGovernment.objects.get(name=country_name)
    print("selected Local Gov ", selected_localgov)

    all_ward = selected_localgov.ward_set.all()
    for ward in all_ward:
        print("city name", ward.name)

        result_set.append({'name': ward.name})

    return JsonResponse(result_set, safe=False)


def get_pooling_unit(request):
    # country_name = request.POST['country_name']
    country_name = request.GET['cnt']

    print("ajax country_name ", country_name)

    result_set = []
    all_lga = []

    answer = str(country_name[1:-1])
    selected_pooling_unit = Ward.objects.get(name=country_name)
    print("selected state name ", selected_pooling_unit)

    all_pooling_unit = selected_pooling_unit.poolingunit_set.all()
    for pooling_unit in all_pooling_unit:
        print("city name", pooling_unit.name)

        result_set.append({'name': pooling_unit.name})

    return JsonResponse(result_set, safe=False)