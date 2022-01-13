from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

# Create your models here.
@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(person_of=instance)
        print("profile created")
post_save.connect(create_profile,sender=User)

 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(person_of=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()


