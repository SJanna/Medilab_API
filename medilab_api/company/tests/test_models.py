from django.test import TestCase

from authentication.models import User, Role
from exam.models import Tariff
from company.models import Company, MissionCompany

class CompanyModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="CompanyAdmin")
        self.user = User.objects.create(
            username="companytest",
            roles=self.role,
            identification_type="IDType",
            identification_number="901234",
            email="companytest@example.com"
        )
        self.company = Company.objects.create(
            user=self.user,
            nit="123456789",
            name="TestCompany",
            AKA="TC",
            address="123 Test St",
            department="TestDepartment",
            city="TestCity",
            email="companytest@example.com",
            phone="1234567890"
        )
        
    def test_company_creation(self):
        self.assertTrue(Company.objects.exists())
        
    def test_company_string_representation(self):
        self.assertEqual(str(self.company), "companytest")
        
    # Additional tests for the company model can be added here

class MissionCompanyModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="CompanyAdmin")
        self.user = User.objects.create(
            username="missioncompanytest",
            roles=self.role,
            identification_type="IDType",
            identification_number="567890123",
            email="missioncompanytest@example.com"
        )
        self.company = Company.objects.create(
            user=self.user,
            nit="987654321",
            name="MissionTestCompany",
            AKA="MTC",
            address="321 Test St",
            department="TestDepartment",
            city="TestCity",
            email="missioncompanytest@example.com",
            phone="0987654321"
        )
        self.mission_company = MissionCompany.objects.create(
            name="TestMission",
            company=self.company,
            active=True
        )
        
    def test_mission_company_creation(self):
        self.assertTrue(MissionCompany.objects.exists())
        
    def test_mission_company_relations(self):
        self.assertEqual(self.mission_company.company, self.company)
        
    # Additional tests for the mission company model can be added here

