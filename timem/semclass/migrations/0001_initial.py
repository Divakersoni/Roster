# Generated by Django 2.0.1 on 2018-01-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section', models.CharField(max_length=10)),
                ('shift', models.SmallIntegerField(choices=[(0, 'I'), (1, 'II')], default=0)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.SmallIntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Department')),
            ],
        ),
        migrations.AddField(
            model_name='sec',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semclass.Sem'),
        ),
    ]
