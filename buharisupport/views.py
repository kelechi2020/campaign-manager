from crispy_forms.helper import FormHelper
from django import forms
from django.shortcuts import render
from buharisupport.models import Members, STATE_CHOICE


class Form_applicant(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Surname', required=True)
    mothers_maiden_name = forms.CharField(label='Mothers Maiden Name')
    address = forms.CharField(label='Address', required=True)
    state = forms.ChoiceField(label='State', required=True, choices=STATE_CHOICE)
    local_government = forms.CharField(label='Local Government', widget=forms.ChoiceField)
    district = forms.CharField(label='District')
    landmark_identity = forms.CharField(label='Landmark')
    phone_number = forms.CharField(label='Phone Number', required=True)
    email = forms.EmailField(label='E-mail')
    communication_means2 = forms.BooleanField(label='Second Means Of Communication')
    communication_means1 = forms.BooleanField(label='Ist Means Of Communication', required=True)
    class Meta:
        model = Members
        fields = ['first_name','last_name','mothers_maiden_name','address','state','local_government',
                  'district','landmark_identity','phone_number','email','communication_means1','communication_means2']

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False  # don't render form DOM element
        helper.render_unmentioned_fields = True  # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-4'
        return helper


def page(request):
    if request.POST:

        first_name = request.POST.get("first_name")
        last_name = request.POST.get('last_name')
        mothers_maiden_name = request.POST.get('mothers_maiden_name')
        address = request.POST.get('address')
        states = request.POST.get('states')
        local_government = request.POST.get('local_government')
        district = request.POST.get('district')
        landmark_identity = request.POST.get('landmark_identity')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        communication_means1 = request.POST.get('communication_means1')
        communication_means2 = request.POST.get('communication_means2')

        new_applicant = Members(first_name=first_name, last_name=last_name,
                                      mothers_maiden_name=mothers_maiden_name,
                                      address=address, state=states, local_government=local_government,
                                      district=district, landmark_identity=landmark_identity,
                                      phone_number=phone_number, email=email, sex=sex,
                                      communication_means2=communication_means2,
                                      communication_means1=communication_means1)

        new_applicant.save()
        success = 1
        return render(request, 'index_inner.html', {'success': success})
    else:
        return render(request, 'bso/index.html')

