# Generated by Django 4.2.1 on 2023-08-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_alter_useraccount_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='id',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
