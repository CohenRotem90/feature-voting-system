from django.db import models
from django.contrib.auth.models import User

class FeatureRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def vote_count(self):
        return self.vote_set.count()

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature = models.ForeignKey(FeatureRequest, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'feature')