# Generated by Django 4.2.1 on 2023-06-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_ichimlik_rasm_alter_xodim_rasm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ichimlik',
            name='rasm',
            field=models.FileField(upload_to='ichimlik/'),
        ),
        migrations.AlterField(
            model_name='xodim',
            name='rasm',
            field=models.FileField(upload_to='xodim/'),
        ),
        migrations.AlterField(
            model_name='yangilik',
            name='rasm',
            field=models.FileField(upload_to='yangilik/'),
        ),
    ]