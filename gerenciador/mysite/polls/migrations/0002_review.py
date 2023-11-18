# Generated by Django 4.2.7 on 2023-11-17 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_title', models.CharField(max_length=85)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.task')),
            ],
        ),
    ]
