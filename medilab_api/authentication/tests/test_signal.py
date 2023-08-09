

from unittest import TestCase

from ..models import Role


class SignalsTest(TestCase):
    def test_post_migrate_signal(self):
        roles = ['Admin', 'Doctor', 'Patient']
        for role_name in roles:
            self.assertTrue(Role.objects.filter(name=role_name).exists())