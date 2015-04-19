from django.test import TestCase
import datetime
from django.utils import timezone
from SystemObjects.models import User
#Here are all the code based tests to be conducted (as of right now)

"""
Format for declaring a test is as follows
Preconditions:
Test Description:
Expected Outcome:
"""


class SystemObject_tests(TestCase):
    #1 Patient sign up
    """
    Preconditions: Patients are in the system, data is filled out.
    Test Description: A test patient will be signed up
    Expected Outcome: Patients should be able to provide information to the system,
    patients should not be able to sign up without health insurance.
    """
    def setup():
        patient = User(first_name = 'fred')
        
    def test_patient_sign_up(self):
        self.assertEqual(patient.name, 'fred')

