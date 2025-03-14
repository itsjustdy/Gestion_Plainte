from django.test import TestCase
from .models import Issue

class IssueModelTest(TestCase):

    def setUp(self):
        self.issue = Issue.objects.create(
            description="Route endommagée",
            status="Signalé",
            location="Rue de la Paix",
            date_reported="2023-10-01"
        )

    def test_issue_creation(self):
        self.assertEqual(self.issue.description, "Route endommagée")
        self.assertEqual(self.issue.status, "Signalé")
        self.assertEqual(self.issue.location, "Rue de la Paix")

    def test_issue_str(self):
        self.assertEqual(str(self.issue), "Route endommagée - Signalé")