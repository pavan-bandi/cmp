# Generated by Django 4.0.4 on 2022-09-26 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentss',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=50)),
                ('profile_pic', models.FileField(upload_to='')),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='clmt.courses')),
                ('session_year_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clmt.sessionyearmodel')),
            ],
        ),
    ]
