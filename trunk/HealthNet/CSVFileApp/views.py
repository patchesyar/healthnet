from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
from .forms import ProfileImageForm
from .models import ProfileImage

# Create your views here.
#Author: Michael Elgin
"""Notes
-"creation" function is done
-"processing is mostly done. We need to find a way to give the file to the variable "file" so that
the rest of the code can make use of its contents. Also, the if blocks that i have noted need to still
be filled out need to contain code that generates a user of the respective type into the system.
"""
def creation(request):
    return render_to_response('CSVPage.html')

def processing(request):
    #Here is the main process for creating the user from the CSV File

    # give the file name from the html page
    fileName = None  # this needs to be given by a textfield on the page, or in some other way

    # make sure the file can be opened
    try:
        file = open(fileName)
    except:
        # do something to tell the user that the program was unable to find the file
        return render_to_response('CSVFailure.html')
        # return render_to_response('CSVInvalid.html')#for testing the html file
        # return render_to_response('CSVSuccess.html')#for testing the html file

    # process the file's info
    currWord = ''
    for line in file:
        wordList = []  # set the wordlist as empty
        for char in line:  # for every character
            if char ==',':  # append the currword if a comma has been reached
                wordList.append(currWord)
                currWord = ''  # reset the currword
            else:  # add the current char to the currword
                currWord+=char
        typeWord = wordList[0].lower()  # lowercase so we don't have to deal with uppercase
        if (typeWord!='doctor') and (typeWord!='nurse') and (typeWord!='admin') and (typeWord!='patient'): 
            # do something to tell the user they have an invalid format
            return render_to_response('CSVInvalid.html')
        else:  # create a user using the line's data
            if typeWord=='doctor':
                # create doctor user in the system,this still needs to be filled out
                pass
            if typeWord=='nurse':
                # create nurse user in the system,this still needs to be filled out
                pass
            if typeWord=='admin':
                # create admin user in the system,this still needs to be filled out
                pass
            if typeWord=='patient':
                # create patient user in the sytem,this still needs to be filled out
                pass

    # do something to tell the users from the CSV file were generated into the system
    return render_to_response('CSVSuccess.html')


def johnsImplementationOfLines32To40(self):
    for line in file:
        wordList[0]=wordList[0].lower()  # convert the first word to lowercase, may not be needed
        typeWord = wordList[0]  # save the first word into typeWord.
                                # Can also use typeWord=wordList[0].lower if omitting line 65

#These are some class based views that Mike is testing to attempt to get file uploading to work.
class ProfileImageView(FormView):
    template_name = 'file_upload.html'
    form_class = ProfileImageForm

    def form_valid(self):
        profile_image = ProfileImage(
            image = self.get_form_kwargs().get('files'))
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile_image', kwargs = {'pk': self.id})

class ProfileDetailView(DetailView):
    model = ProfileImage
    template_name= 'file_upload.html'
    context_object_name = 'image'

class ProfileImageIndexView(ListView):
    model = ProfileImage
    template_name = 'file_upload.html'
    context_object_name = 'images'
    queryset = ProfileImage.objects.all()
