# Generated by Django 5.1.3 on 2024-11-05 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('is_employer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customuser')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.job')),
            ],
        ),
    ]