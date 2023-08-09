from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from ..models import Role, User, Doctor, Patient

class RoleModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="TestRole")
        
    def test_role_creation(self):
        self.assertTrue(Role.objects.exists())
        
    def test_role_string_representation(self):
        self.assertEqual(str(self.role), "TestRole")

class UserModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="TestRole")
        self.user = User.objects.create(
            username="testuser",
            roles=self.role,
            identification_type="IDType",
            identification_number="123456",
            email="testuser@example.com"
        )
        
    def test_user_creation(self):
        self.assertTrue(User.objects.exists())
        
    def test_user_string_representation(self):
        self.assertEqual(str(self.user), "testuser")
    
    # Additional tests like checking cascading deletes can be added here

class DoctorModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="Doctor")
        self.user = User.objects.create(
            username="doctortest",
            roles=self.role,
            identification_type="IDType",
            identification_number="789012",
            email="doctortest@example.com"
        )
        self.doctor = Doctor.objects.create(user=self.user, specialty="Cardiologist")
        
    def test_doctor_creation(self):
        self.assertTrue(Doctor.objects.exists())
        
    def test_doctor_string_representation(self):
        self.assertEqual(str(self.doctor), "doctortest")
        
    # Additional tests for the doctor model can be added here

class PatientModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="Patient")
        self.user = User.objects.create(
            username="patienttest",
            roles=self.role,
            identification_type="IDType",
            identification_number="345678",
            email="patienttest@example.com"
        )
        self.patient = Patient.objects.create(user=self.user, medical_record_number="MRN001", date_of_birth="2002-05-25")
        
    def test_patient_creation(self):
        self.assertTrue(Patient.objects.exists())
        
    def test_patient_string_representation(self):
        self.assertEqual(str(self.patient), "patienttest")
        
    # Additional tests for the patient model can be added here


