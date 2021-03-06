# Generated by Django 2.0.1 on 2018-01-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], default=0)),
                ('department_name', models.CharField(max_length=100)),
                ('department_initials', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_initials', models.CharField(max_length=10)),
                ('type_subject', models.SmallIntegerField(choices=[(0, 'Theory'), (1, 'Lab')], default=0)),
                ('semester', models.SmallIntegerField()),
                ('subject_code', models.CharField(max_length=10)),
                ('teaching_hours_per_week', models.SmallIntegerField()),
                ('teaching_hours_a_day', models.SmallIntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_initials', models.CharField(blank=True, max_length=10)),
                ('DOJ', models.CharField(blank=True, max_length=10)),
                ('designation', models.CharField(max_length=100)),
                ('teaching_hours_per_week', models.SmallIntegerField()),
                ('shift', models.SmallIntegerField(choices=[(0, 'I'), (1, 'II')], default=0)),
                ('teaching_hours_a_day_subject1', models.SmallIntegerField(default=0)),
                ('teaching_hours_a_day_subject2', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('teaching_hours_a_day_subject3', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('teaching_hours_a_day_subject4', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('total_teaching_hours_a_day', models.SmallIntegerField(default=4)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Department')),
                ('subject1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject1', to='teacher.Subject')),
                ('subject2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='teacher.Subject')),
                ('subject3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject3', to='teacher.Subject')),
                ('subject4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject4', to='teacher.Subject')),
            ],
        ),
    ]
