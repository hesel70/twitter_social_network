# Generated by Django 4.2.2 on 2023-06-19 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='user.account')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='user.account')),
            ],
        ),
    ]
