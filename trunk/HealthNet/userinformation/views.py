from django.http import HttpResponse
from userinformation.models import UserProfile
from django.contrib.auth.decorators import login_required
import datetime
# Note: During code refactoring, django.shortcuts.render, django.shortcuts.get_object_or_404,
# django.http.HttpResponseRedirect, and #django.contrib.auth.models.User were removed as
# unused imports. If needed in future development, reinclude them.

@login_required(login_url='/login/')
def main_page(request):
    thisUser = request.user
    try:  # Attempt to get UserProfile for user if existing
        thisProfile = UserProfile.objects.get(user=thisUser)
    except UserProfile.DoesNotExist:  # Initialize an empty UserProfile for user without one
        thisProfile = UserProfile(user=thisUser,
                                  insuranceid=0,
                                  hospital=' ',
                                  birthday=datetime.date.today(),
                                  phone=0,
                                  emergency_firstname=' ',
                                  emergency_lastname=' ',
                                  emergency_phone=0,
                                  allergies=' ',
                                  recent_operations=' ',
                                  gender=' ',
                                  prescriptions=' ')  # end UserProfile
    thisProfile.insurance_id = request.POST.get('ID')
    thisProfile.hospital = request.POST.get('prefHos')
    thisProfile.birthday = request.POST.get('dob')
    thisProfile.phone = request.POST.get('phone')
    thisProfile.emergency_firstname = request.POST.get('efirstName')
    thisProfile.emergency_lastname = request.POST.get('elastName')
    thisProfile.emergency_phone = request.POST.get('ePhone')
    thisProfile.allergies = request.POST.get('allergies')
    thisProfile.recent_operations = request.POST.get('recentOps')
    thisProfile.gender = request.POST.get('gender')
    thisProfile.prescriptions = request.POST.get('prescriptions')
    thisProfile.save()
    return HttpResponse("Your name is " + thisUser.username +
                        ", your insurance id is " + str(thisProfile.insurance_id) +
                        ", and your gender is " + str(thisProfile.gender))
