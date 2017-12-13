from django.shortcuts import render

from buharisupport.models import LocalGovernment, Members


def page(request, state):
    localgov = LocalGovernment.objects.filter(country__name=state)
    applicant_number = [Members.objects.filter(local_government=state).count() for state in localgov]
    new = zip(localgov, applicant_number)
    return render(request, 'localgovernments.html',{'new':new, 'state':state} )