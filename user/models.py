from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    email = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.full_name


class UserRelative(models.Model):
    RELATIVE_LEVEL_CHOICES = (
        ('father', 'Ota'),
        ('mather', 'Ona'),
    )
    user = models.ForeignKey(User, related_name='relative', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    email = models.CharField(max_length=150)
    relative_level = models.CharField(max_length=20, choices=RELATIVE_LEVEL_CHOICES, default='father')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.full_name
