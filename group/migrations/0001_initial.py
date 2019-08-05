# Generated by Django 2.2.3 on 2019-08-05 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('GroupPid', models.AutoField(primary_key=True, serialize=False)),
                ('GroupName', models.CharField(max_length=100, unique=True)),
                ('GroupPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nickname', models.CharField(max_length=100)),
                ('GroupPid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
    ]
