# Generated by Django 4.2.13 on 2024-07-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empleados', models.ManyToManyField(to='empleados.empleado')),
            ],
        ),
    ]