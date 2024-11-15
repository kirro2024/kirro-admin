from django.db import models


class UserProfile(models.Model):
    user_id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(unique=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    phone_number = models.TextField(unique=True, blank=True, null=True)
    profile_picture_url = models.TextField(blank=True, null=True)
    resume_url = models.TextField(blank=True, null=True)
    job_preferences = models.JSONField(blank=True, null=True)  
    userlocation = models.TextField(db_column='userLocation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user_profile'


    def __str__(self):
        return self.email