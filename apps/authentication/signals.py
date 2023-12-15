from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from apps.user.models.information import UserInformationModel
from apps.estadisticas.models.stats import UserStatsModel

@receiver(post_save, sender=User)
def _post_save_user(sender, instance, **kwargs):
    if not instance.password.startswith('pbkdf2'):
        instance.password = make_password(instance.password)
        instance.save()
    if not hasattr(instance, 'information'):
        UserInformationModel.objects.create(user=instance)

@receiver(post_migrate)
def create_default_users(sender, **kwargs):
    users_db = User.objects
    information_db = UserInformationModel.objects
    stats_db = UserStatsModel.objects

    try:
        # Crea el usuario administrador predeterminado
        if not users_db.filter(username='admin'):
            admin_user = users_db.create_superuser('admin', 'admin@yopmail.com', '1234')

            admin_information = {
                'user': admin_user,
                'identification': 'admin_id',
                'user_type': 0
            }

            # information_db.create(**admin_information)
            existing_information = UserInformationModel.objects.filter(user=admin_user).first()
            if existing_information:
                existing_information.delete()
                information_instance = information_db.create(user=admin_user, identification=admin_information['identification'], user_type=admin_information['user_type'])
            else:
                print(f'Información para el usuario {username} ya existe.')
                print('🥳 ¡Usuario administrador creado!')
    except Exception as e:
        print(f'Error al crear el usuario administrador: {e}')

    # Lista de usuarios a crear
    users_to_create = [
        {
            'username': 'lider@yopmail.com',
            'email': 'lider@yopmail.com',
            'password': '1234',
            'information': {
                "identification": "1151898",
                "user_type": 6
            }
        },
        {
            'username': 'docente@yopmail.com',
            'email': 'docente@yopmail.com',
            'password': '1234',
            'information': {
                "identification": "1151891",
                "user_type": 6
            }
        }
    ]

    for user_data in users_to_create:
        information_data = user_data['information']
        username = user_data['username']
        email = user_data['email']
        password = user_data['password']
        
        user_instance, created = users_db.get_or_create(username=username, email=email, defaults={'password': password})
        stats_instance = stats_db.get_or_create(user=user_instance)
        existing_information = UserInformationModel.objects.filter(user=user_instance).first()
        
        #print(f'🎈🎈🎈🎈🎈🎈🎈🎈🎈{existing_information}')

        if existing_information:
            existing_information.delete()
            information_instance = information_db.create(user=user_instance, identification=information_data['identification'], user_type=information_data['user_type'])
            #print(f'🎈🎈🎈🎈🎈🎈🎈🎈🎈{information_instance.id}')
        else:
            print(f'Información para el usuario {username} ya existe.')
