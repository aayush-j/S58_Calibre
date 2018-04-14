# Generated by Django 2.0.1 on 2018-01-14 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180114_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='exam',
            name='end_datetime',
            field=models.DateTimeField(blank=True, help_text='Enter time in HH:MM format.', null=True, verbose_name='End Date & Time'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_datetime',
            field=models.DateTimeField(blank=True, help_text='Enter time in HH:MM format.', null=True, verbose_name='Start Date & Time'),
        ),
        migrations.AddField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Course'),
        ),
    ]
