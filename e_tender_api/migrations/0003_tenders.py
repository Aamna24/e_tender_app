# Generated by Django 3.1.2 on 2020-12-12 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('e_tender_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('telecom', 'Telecom'), ('construction', 'Construction'), ('it', 'IT'), ('medical', 'Medical'), ('electrical', 'Electrical'), ('oil and gas', 'Oil and Gas'), ('others', 'Others')], default='Construction', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
                ('availibility', models.CharField(choices=[('inactive', 'Inactive'), ('active', 'Active')], default='active', max_length=10)),
                ('region', models.CharField(default='', max_length=20)),
                ('description', models.TextField(default='')),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, null=True, region=None, unique=True)),
                ('opening_date', models.DateField(default='')),
                ('last_date', models.DateField(default='')),
                ('upload', models.FileField(default='', upload_to='uploads/')),
                ('organization_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]