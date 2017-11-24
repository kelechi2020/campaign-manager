from django.shortcuts import render

from buharisupport.models import LocalGovernment, Members,PoolingUnit


def page(request, ward):
    pooling_unit = PoolingUnit.objects.filter(ward__ward_name=ward)
    pooling_unit_number = [Members.objects.filter(pooling_unit=count).count() for count in pooling_unit]
    from pprint import pprint
    pprint(pooling_unit_number)
    new = zip(pooling_unit,pooling_unit_number)
    return render(request, 'pooling_unit_analysis.html',{'new':new, 'state':ward} )
