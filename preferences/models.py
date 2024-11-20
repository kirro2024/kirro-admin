from django.db import models


class UserProfile(models.Model):
    user_id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    profile_picture_url = models.CharField(max_length=255,blank=True, null=True)
    resume_url = models.CharField(max_length=255,blank=True, null=True)
    job_preferences = models.JSONField(blank=True, null=True)  
    

    class Meta:
        managed = False
        db_table = 'user_profile'


    def __str__(self):
        return self.email