# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-08 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djcrm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('comment_user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leaduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Title')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('website', models.CharField(blank=True, max_length=255, verbose_name='Website')),
                ('status', models.CharField(blank=True, choices=[('assigned', 'Assigned'), ('in process', 'In Process'), ('converted', 'Converted'), ('recycled', 'Recycled'), ('dead', 'Dead')], max_length=255, verbose_name='Status of Lead')),
                ('source', models.CharField(blank=True, choices=[('call', 'Call'), ('email', 'Email'), ('existing customer', 'Existing Customer'), ('partner', 'Partner'), ('public relations', 'Public Relations'), ('compaign', 'Campaign'), ('other', 'Other')], max_length=255, verbose_name='Source of Lead')),
                ('opportunity_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Opportunity Amount')),
                ('description', models.TextField()),
                ('phone', models.IntegerField(null=True)),
                ('teams', models.CharField(choices=[('SALES', 'SALES'), ('SUPPORT', 'SUPPORT'), ('TOP MANAGEMENT', 'TOP MANAGEMENT')], max_length=255, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Leads', to='accounts.LeadAccount')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leadaddress', to='djcrm.Address')),
                ('assigned_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Leaduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='leadid',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.Lead'),
        ),
    ]
