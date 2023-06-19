# Generated by Django 4.2.2 on 2023-06-19 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_follow'),
        ('post', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('alt', models.CharField(max_length=100, verbose_name='Alternative Text')),
                ('image', models.FileField(upload_to='uploads/photos', verbose_name='Image')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.comment', verbose_name='Parent Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.account', verbose_name='Account')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comment',
            },
        ),
    ]