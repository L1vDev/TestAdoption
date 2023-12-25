# Generated by Django 4.2.3 on 2023-09-16 16:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('identity', models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)], verbose_name='CI')),
                ('first_name_adopter', models.CharField(max_length=25, verbose_name='Nombre')),
                ('last_name_adopter', models.CharField(max_length=75, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Vacunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacuna', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre:')),
                ('age', models.IntegerField(verbose_name='Edad:')),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('exit_date', models.DateField(blank=True, null=True)),
                ('is_adopted', models.BooleanField(default=False)),
                ('vacunas', models.ManyToManyField(blank=True, to='mascotas.vacunas', verbose_name='Vacunas:')),
            ],
        ),
        migrations.CreateModel(
            name='AdoptionsRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adoption_date', models.DateField(auto_now_add=True)),
                ('adopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.adopter')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.mascotas')),
            ],
        ),
    ]
