from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from apps.user.models.information import UserInformationModel


@receiver(post_save, sender=User)
def _post_save_user(sender, instance, **kwargs):
    if not instance.password.startswith('pbkdf2'):
        instance.password = make_password(instance.password)
        instance.save()
    if not hasattr(instance, 'information'):
        UserInformationModel.objects.create(user=instance)


# Create default user admin
@receiver(post_migrate)
def created_user_admin(sender, **kwargs):
    users_db = User.objects
    user_admin= {
                'username': 'admin',
                'email': 'admin@yopmail.com',
                'password': '1234'
                }
    
    if not users_db.filter(username=user_admin['username']).exists():
        users_db.create_superuser(**user_admin)
