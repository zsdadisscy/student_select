from django.test import TestCase
from models import Tutor
# Create your tests here.

obj = Tutor.objects.filter(username='123')