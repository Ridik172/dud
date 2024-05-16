# Generated by Django 5.0.3 on 2024-05-15 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('idad', models.AutoField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('Description', models.CharField(default='Занимаюсь:', max_length=99)),
                ('Telephone', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'Ads',
            },
        ),
        migrations.CreateModel(
            name='CategoriesTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'idcategories_types_idtag',
            },
        ),
        migrations.CreateModel(
            name='CategoriesTypes',
            fields=[
                ('idcategories_types', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=33)),
            ],
            options={
                'db_table': 'categories_types',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('idcom', models.AutoField(primary_key=True, serialize=False)),
                ('Textcom', models.CharField(default='да, он хорош', max_length=99)),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='ServiceTypes',
            fields=[
                ('idservice_types', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=33)),
            ],
            options={
                'db_table': 'service_types',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('idtag', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(default='Для:', max_length=33)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.RemoveConstraint(
            model_name='users',
            name='unique_phone',
        ),
        migrations.RemoveConstraint(
            model_name='users',
            name='unique_email',
        ),
        migrations.RemoveConstraint(
            model_name='users',
            name='check_phone',
        ),
        migrations.RemoveConstraint(
            model_name='users',
            name='check_birthdate',
        ),
        migrations.AlterField(
            model_name='users',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='users',
            name='Middlename',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
        migrations.AddField(
            model_name='ads',
            name='iduser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.users'),
        ),
        migrations.AddField(
            model_name='categoriestag',
            name='idcategories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.categoriestypes'),
        ),
        migrations.AddField(
            model_name='ads',
            name='idcategories_types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.categoriestypes'),
        ),
        migrations.AddField(
            model_name='comment',
            name='adid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ads'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.users'),
        ),
        migrations.AddField(
            model_name='servicetypes',
            name='idcategories_types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.categoriestypes'),
        ),
        migrations.AddField(
            model_name='categoriestag',
            name='idtag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.tag'),
        ),
        migrations.AlterUniqueTogether(
            name='categoriestag',
            unique_together={('idcategories', 'idtag')},
        ),
    ]