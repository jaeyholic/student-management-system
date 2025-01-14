# Generated by Django 3.0.7 on 2020-06-21 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20200621_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('feedback', models.TextField(blank=True, default='')),
                ('approved', models.BooleanField(default=False)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Project')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
