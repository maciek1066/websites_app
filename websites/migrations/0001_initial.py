# Generated by Django 2.0.7 on 2018-07-09 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=128, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=32)),
                ('meta_description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=32)),
                ('meta_description', models.CharField(max_length=128)),
                ('alexa_rank', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='website',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.WebsiteCategory'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.Website'),
        ),
    ]