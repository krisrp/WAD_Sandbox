# Generated by Django 3.0.5 on 2020-04-09 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_owner_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Owner'),
        ),
    ]
