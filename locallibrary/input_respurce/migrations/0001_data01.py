# Generated by Django 3.0.1 on 2020-01-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=20)),
                ('Uname', models.CharField(max_length=20)),
                ('Rollno', models.IntegerField()),
                ('Avgmarks', models.IntegerField()),
                ('Phno', models.IntegerField()),
            ],
        ),
    ]
