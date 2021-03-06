# Generated by Django 2.0.1 on 2018-01-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        ('location', '0001_initial'),
        ('semclass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab_final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('day_type', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thrusday'), (5, 'Friday'), (6, 'Saturday')], default=1)),
                ('p1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('lab_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Master_final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_type', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thrusday'), (5, 'Friday'), (6, 'Saturday')], default=1)),
                ('p1', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p2', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p3', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p4', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p5', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p6', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semclass.Sec')),
            ],
        ),
        migrations.CreateModel(
            name='Room_final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_type', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thrusday'), (5, 'Friday'), (6, 'Saturday')], default=1)),
                ('p1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('Room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaching_hours', models.SmallIntegerField(default=0)),
                ('day_type', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=1)),
                ('p1', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p2', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p3', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p4', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p5', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('p6', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
    ]
