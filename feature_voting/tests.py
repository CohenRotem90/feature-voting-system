from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import FeatureRequest, Vote
from django.urls import reverse

class FeatureVotingTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.feature = FeatureRequest.objects.create(title="Test Feature", description="Test Desc", created_by=self.user)

    def test_login_required_redirect(self):
        response = self.client.get(reverse('feature_list'))
        self.assertRedirects(response, '/login/?next=/')

    def test_feature_list_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('feature_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Feature")

    def test_create_feature(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('feature_create'), {
            'title': 'New Feature',
            'description': 'New description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(FeatureRequest.objects.count(), 2)

    def test_vote_feature_once(self):
        self.client.login(username='testuser', password='testpass')
        response1 = self.client.post(reverse('vote_feature', args=[self.feature.id]))
        response2 = self.client.post(reverse('vote_feature', args=[self.feature.id]))
        self.assertEqual(Vote.objects.filter(feature=self.feature, user=self.user).count(), 1)