from django.test import TestCase

# Create your tests here.
from ..models import Tariff, Exam, Package, ExamPrice


class TariffModelTest(TestCase):
    def setUp(self):
        self.tariff = Tariff.objects.create(name="TestTariff", active=True)

    def test_tariff_creation(self):
        self.assertTrue(Tariff.objects.exists())

    def test_tariff_string_representation(self):
        self.assertEqual(str(self.tariff), self.tariff.name)


class ExamModelTest(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(name="TestExam")

    def test_exam_creation(self):
        self.assertTrue(Exam.objects.exists())

    def test_exam_string_representation(self):
        self.assertEqual(str(self.exam), self.exam.name)


class PackageModelTest(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(name="TestExam")
        self.package = Package.objects.create(name="TestPackage", price=100)
        self.package.exams.add(self.exam)

    def test_package_creation(self):
        self.assertTrue(Package.objects.exists())

    def test_package_string_representation(self):
        self.assertEqual(str(self.package), self.package.name)

    def test_package_exam_relation(self):
        self.assertTrue(self.exam in self.package.exams.all())


class ExamPriceModelTest(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(name="TestExam")
        self.exam_price = ExamPrice.objects.create(exam=self.exam, price=100)

    def test_exam_price_creation(self):
        self.assertTrue(ExamPrice.objects.exists())

    def test_exam_price_string_representation(self):
        self.assertEqual(str(self.exam_price), self.exam.name +
                         ' - ' + str(self.exam_price.price))
