# Generated by Django 2.0.1 on 2018-01-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        ('semclass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], default=0)),
                ('room_no', models.CharField(max_length=10)),
                ('alt_name', models.CharField(default='LH1', max_length=10, null=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='teacher.Department')),
                ('sec1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec1', to='semclass.Sec')),
                ('sec2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec2', to='semclass.Sec')),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], default=0)),
                ('lab_no', models.CharField(max_length=10)),
                ('alt_name', models.CharField(default='cp1', max_length=10, null=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='teacher.Department')),
                ('subject1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub1', to='teacher.Subject')),
                ('subject2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub2', to='teacher.Subject')),
                ('subject3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub3', to='teacher.Subject')),
                ('subject4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub4', to='teacher.Subject')),
            ],
        ),
    ]
