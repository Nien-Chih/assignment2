# Generated by Django 4.1.3 on 2022-11-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='lecturer_email',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturer',
            name='lecturer_fname',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturer',
            name='lecturer_lname',
            field=models.CharField(default='Tets', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.CharField(default='2h32', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_fname',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_lname',
            field=models.CharField(default='2y2', max_length=200),
            preserve_default=False,
        ),
    ]
