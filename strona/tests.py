from django.test import TestCase
from django.contrib.auth.models import User
from .models import Entry

class EntryTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("test", "tester@localhost", "123not4")
        Entry.objects.create(title="Some title", content="No content yet, well", author=User.objects.get(username="test"))
    def test_author_existent(self):
        entry = Entry.objects.get(title="Some title")
        user = User.objects.get(username="test")
        self.assertEqual(entry.author, user)
