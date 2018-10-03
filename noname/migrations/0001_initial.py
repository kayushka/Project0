# Generated by Django 2.1.2 on 2018-10-03 10:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.IntegerField(choices=[(1, 'Jedzenie dom'), (2, 'Jedzenie na mieście'), (3, 'Jedzenie w pracy'), (4, 'Alkohol'), (5, 'Czynsz'), (6, 'Woda'), (7, 'Prąd'), (8, 'Gaz'), (9, 'Ogrzewanie'), (10, 'Wywóz śmieci'), (11, 'Naprawy'), (12, 'Wyposażenie'), (13, 'Ubezpieczenie'), (14, 'Paliwo'), (15, 'Naprawa'), (16, 'Wyposażenie'), (17, 'Ubezpieczenie'), (18, 'Bilety'), (19, 'Taxi'), (20, 'Telefon'), (21, 'Telewizja'), (22, 'Internet'), (23, 'Lekarz'), (24, 'Badania'), (25, 'Leki'), (26, 'Ubrania'), (27, 'Buty'), (28, 'Kosmetyki'), (29, 'Chemia domowa'), (30, 'Fryzjer'), (31, 'Art. szkolne'), (32, 'Zajęcia dodatkowe'), (33, 'Szkoła'), (34, 'Gry/zabawki'), (35, 'Opieka nad dziećmi'), (36, 'Sport'), (37, 'Kino/teatr'), (38, 'Koncert'), (39, 'Książki'), (40, 'Prezenty'), (41, 'Oszczędności'), (42, 'Hotel/turystyka'), (43, 'Hobby'), (44, 'Edukacja'), (45, 'Oprogramowanie'), (46, 'Szkolenia'), (47, 'Inne')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('category', models.IntegerField(choices=[(1, 'Pensja'), (2, 'Pensja partnerki/partnera'), (3, 'Premia'), (4, 'Sprzedaż'), (5, 'Inne')])),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]