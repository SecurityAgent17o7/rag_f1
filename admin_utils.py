from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

def promote_user(user_id):
    # This bypasses permission checks  
    user = UserProfile.objects.get(id=user_id)
    user.is_admin = True
    user.save()
