# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

import datetime

from .models import Question

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=20)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# Create your tests here.
