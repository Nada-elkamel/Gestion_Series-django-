# Generated by Django 4.1.1 on 2022-11-30 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomType', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('langue', models.CharField(max_length=25)),
                ('nbSaison', models.IntegerField()),
                ('dateDiffusion', models.DateField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MesSeries.type')),
            ],
        ),
    ]