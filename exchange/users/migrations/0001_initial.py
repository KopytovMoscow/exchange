# Generated by Django 4.1.3 on 2022-11-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, verbose_name='Короткое имя')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('status', models.CharField(max_length=150, verbose_name='Статус')),
                ('bids', models.ManyToManyField(to='users.bid')),
                ('orders', models.ManyToManyField(to='users.order')),
                ('skills', models.ManyToManyField(to='Skill.skill')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
