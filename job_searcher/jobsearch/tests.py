from django.test import TestCase
from jobsearch.models import *

# Create your tests here.
class JobTestCase(TestCase):
    def setUp(self):
        self.job = Job.objects.create(title = 'Junior Software Developer', company = 'Barclays', location = 'Glasgow', description = 'Developing developy things')

    def test_job_saved(self):
        self.assertGreater(self.job.pk, 0)
