from django.shortcuts import render

from buharisupport.models import LocalGovernment, Members


def page(request, state):
    localgov = LocalGovernment.objects.filter(country__name=state)
    from pprint import pprint
    pprint(state)
    applicant_number = [Members.objects.filter(local_government=state).count() for state in localgov]
    new = zip(localgov,applicant_number)
    from pprint import pprint
    pprint(new)
    return render(request, 'localgovernments.html',{'new':new} )