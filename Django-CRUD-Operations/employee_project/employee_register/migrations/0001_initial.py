# Generated by Django 3.0.1 on 2019-12-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bookname', models.CharField(max_length=20)),
                ('Authorname', models.CharField(max_length=20)),
                ('Subjectname', models.CharField(max_length=20)),
                ('Inventory', models.IntegerField()),
            ],
        ),
    ]
