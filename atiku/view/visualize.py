from django.shortcuts import render

from atiku.models import State, Members


def page(request):
    states = State.objects.all()
    applicant_number = [Members.objects.filter(state=state.name).count() for state in states]
    stateauto = zip(states, applicant_number)
    from pprint import pprint
    pprint(type(applicant_number))
    pprint(type(states))
    pprint(applicant_number)

    return render(request, 'home v3.html', {'stateauto':stateauto})
