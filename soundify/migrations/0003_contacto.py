# Generated by Django 3.2.4 on 2021-06-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundify', '0002_auto_20210611_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('apelido', models.CharField(max_length=64)),
                ('telefone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32)),
                ('dataNascimento', models.DateField()),
            ],
        ),
    ]
