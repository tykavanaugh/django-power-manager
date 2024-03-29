# Generated by Django 3.2.9 on 2021-11-21 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='assignments',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='manager.assignment'),
        ),
        migrations.AlterField(
            model_name='account',
            name='corporation',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ceo', to='manager.corporation'),
        ),
        migrations.AlterField(
            model_name='account',
            name='paramilitary',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='military_leader', to='manager.paramilitary'),
        ),
        migrations.AlterField(
            model_name='account',
            name='party',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='manager.party'),
        ),
        migrations.AlterField(
            model_name='account',
            name='union',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='union_boss', to='manager.union'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='corporations',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corp_sectors', to='manager.corporation'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='unions',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='union_sectors', to='manager.union'),
        ),
    ]
