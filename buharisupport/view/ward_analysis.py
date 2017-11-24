from django.shortcuts import render

from buharisupport.models import LocalGovernment, Members, Ward


def page(request, localgov):
    ward = Ward.objects.filter(local_government__name=localgov)
    ward_number = [Members.objects.filter(ward=count.ward_name).count() for count in ward]
    new = zip(ward,ward_number)
    return render(request, 'ward_analysis.html',{'new':new, 'state':localgov} )