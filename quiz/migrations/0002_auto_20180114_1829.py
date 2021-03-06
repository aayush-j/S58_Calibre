# Generated by Django 2.0.1 on 2018-01-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('radio', 'Radio'), ('select-multiple', 'Select Multiple')], default='radio', max_length=20),
        ),
    ]
