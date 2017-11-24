from django.shortcuts import render

from buharisupport.models import LocalGovernment, Members, Ward


def page(request, localgov):
    ward = Ward.objects.filter(local_government__name=localgov)
    ward_number = [Members.objects.filter(ward=count).count() for count in ward]
    from pprint import pprint
    pprint(ward_number)
    new = zip(ward,ward_number)
    return render(request, 'ward_analysis.html',{'new':new, 'state':localgov} )