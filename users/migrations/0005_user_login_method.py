# Generated by Django 3.0.5 on 2020-04-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200422_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('google', 'google')], default='email', max_length=50),
        ),
    ]
