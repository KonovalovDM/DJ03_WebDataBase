# Generated by Django 5.1.3 on 2024-12-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название новости')),
                ('short_description', models.CharField(max_length=255, verbose_name='Краткое описание новости')),
                ('text', models.TextField(verbose_name='Новость')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('author', models.CharField(max_length=100, verbose_name='Автор публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
