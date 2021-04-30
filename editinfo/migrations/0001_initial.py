# Generated by Django 3.2 on 2021-04-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Q_A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=150)),
                ('score', models.FloatField(blank=True, null=True)),
                ('blog', models.ManyToManyField(to='editinfo.Blog')),
                ('domain', models.ManyToManyField(to='editinfo.Domain')),
                ('project', models.ManyToManyField(to='editinfo.Project')),
                ('q_a', models.ManyToManyField(to='editinfo.Q_A')),
                ('technology', models.ManyToManyField(to='editinfo.Technology')),
            ],
        ),
    ]
