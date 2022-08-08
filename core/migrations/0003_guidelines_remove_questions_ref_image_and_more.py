# Generated by Django 4.0.4 on 2022-07-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_questions_user_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guidelines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='ref_image',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='user',
        ),
    ]
