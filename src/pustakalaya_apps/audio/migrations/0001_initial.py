# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('abstract', models.TextField(blank=True, verbose_name='Abstract/Summary')),
                ('additional_note', models.TextField(blank=True, verbose_name='Additional Note')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('license_type', models.CharField(choices=[('creative commons', 'Creative commons'), ('copyright retained', 'Copyright retained'), ('apache License 2.0', 'Apache license 2.0'), ('creative commons', 'Creative commons'), ('mit license', 'मानोज'), ('custom license', 'Custom License'), ('na', 'Not available')], max_length=255, verbose_name='License type')),
                ('custom_license', models.TextField(blank=True, verbose_name='Rights')),
                ('year_of_available', models.DateField(blank=True, null=True, verbose_name='Year of available')),
                ('publication_year', models.DateField(blank=True, null=True, verbose_name='Publication year')),
                ('place_of_publication', models.CharField(blank=True, max_length=255, verbose_name='Place of publication')),
                ('volume', models.CharField(blank=True, default='', max_length=254)),
                ('edition', models.CharField(blank=True, default='', max_length=254)),
                ('type', models.CharField(default='audio', editable=False, max_length=5)),
                ('audio_running_time', models.CharField(blank=True, max_length=3, verbose_name='Running time in minutes')),
                ('audio_thumbnail', models.ImageField(max_length=255, upload_to='uploads/thumbnails/audio/%Y/%m/%d')),
            ],
            options={
                'db_table': 'audio',
            },
        ),
        migrations.CreateModel(
            name='AudioFileUpload',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('file_name', models.CharField(max_length=255, verbose_name='File name')),
                ('upload', models.FileField(max_length=255, upload_to='uploads/audio/%Y/%m/')),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio')),
            ],
            options={
                'db_table': 'audio_file',
            },
        ),
        migrations.CreateModel(
            name='AudioGenre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('genre', models.CharField(max_length=255, verbose_name='Genre name')),
                ('genre_description', models.TextField(verbose_name='Genre description')),
            ],
            options={
                'db_table': 'audio_genre',
            },
        ),
        migrations.CreateModel(
            name='AudioLinkInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('link_name', models.URLField(verbose_name='Link URL')),
                ('link_description', models.CharField(max_length=500, verbose_name='Link Description')),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio', verbose_name='Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AudioSeries',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('series_name', models.CharField(max_length=255, verbose_name='Series name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'db_table': 'audio_series',
            },
        ),
        migrations.CreateModel(
            name='AudioType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Audio type')),
                ('description', models.TextField(verbose_name='Audio description')),
            ],
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audio.AudioGenre', verbose_name='Audio Genre'),
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_read_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Biography', verbose_name='Read / Voice by'),
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audio.AudioSeries', verbose_name='Audio Series / Volume'),
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_types',
            field=models.ManyToManyField(to='audio.AudioType', verbose_name='Audio types'),
        ),
        migrations.AddField(
            model_name='audio',
            name='collections',
            field=models.ManyToManyField(to='collection.Collection', verbose_name='Add this audio to these collection'),
        ),
        migrations.AddField(
            model_name='audio',
            name='education_levels',
            field=models.ManyToManyField(to='core.EducationLevel', verbose_name='Education Levels'),
        ),
        migrations.AddField(
            model_name='audio',
            name='keywords',
            field=models.ManyToManyField(to='core.Keyword', verbose_name='Select list of keywords'),
        ),
        migrations.AddField(
            model_name='audio',
            name='languages',
            field=models.ManyToManyField(to='core.Language', verbose_name='Languages'),
        ),
        migrations.AddField(
            model_name='audio',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Publisher', verbose_name='Audio publisher'),
        ),
        migrations.AddField(
            model_name='audio',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='core.Sponsor', verbose_name='Sponsor'),
        ),
    ]
