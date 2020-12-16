# Generated by Django 2.2.5 on 2019-09-30 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jiranapp', '0010_auto_20190930_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='invited_by',
            field=models.ForeignKey(on_delete=None, related_name='registered_by', to='jiranapp.Household'),
        ),
        migrations.CreateModel(
            name='EventInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attending', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited_to', to='jiranapp.Event')),
                ('resident', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resident_invited_to', to='jiranapp.Resident')),
                ('visitor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitor_invited_to', to='jiranapp.Visitor')),
            ],
        ),
    ]