# Generated by Django 4.2.8 on 2023-12-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'student_table',
            },
        ),
    ]
