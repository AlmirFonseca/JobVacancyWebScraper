
import unittest
import sys
sys.path.append('./src/job_scraper')
from job_scraper import JobScraper
from unittest.mock import patch

class TestJobScraper(unittest.TestCase):

    def setUp(self):
        # Setup for each test
        self.scraper = JobScraper()

    def test_initialization(self):
        self.assertIsInstance(self.scraper, JobScraper)

    def test_set_valid_options(self):
        data_type = "site_names"
        values = ["LinkedIn", "Indeed"]
        self.assertTrue(self.scraper.set_options(data_type, values))

    def test_set_invalid_options(self):
        data_type = "site_names"
        values = ["LinkedIn", "Invalid"]
        self.assertFalse(self.scraper.set_options(data_type, values))

    def test_get_valid_options(self):
        data_type = "site_names"
        self.assertEqual(self.scraper.get_options(data_type), ["LinkedIn","Indeed","Glassdoor","ZipRecruiter"])

    def get_invalid_options(self):
        data_type = "invalid"
        self.assertIsNone(self.scraper.get_options(data_type))

    def test_job_retrieval(self):
        self.scraper.set_options("site_names", ["LinkedIn", "Indeed"])
        self.scraper.set_options("job_types", ["Tempo integral"])
        self.scraper.set_options("countries", ["Rio de Janeiro"])
        self.scraper.set_options("keywords", ["Cientista de dados"])
        self.scraper.set_options("remote_options", ["Trabalho remoto"])

        self.scraper.get_jobs()

        self.assertIsNotNone(self.scraper.job)

if __name__ == '__main__':
    unittest.main()
