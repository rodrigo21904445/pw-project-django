# Generated by Django 3.2.4 on 2021-07-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundify', '0006_auto_20210702_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('comentario', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]