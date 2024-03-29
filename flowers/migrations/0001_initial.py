# Generated by Django 4.2.9 on 2024-01-03 07:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('img', models.FileField(blank=True, null=True, upload_to='blog/')),
                ('eye', models.IntegerField(blank=True, default=0, null=True)),
                ('like', models.IntegerField(blank=True, default=0, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('img', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cotent', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('rank', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('price', models.CharField(max_length=250)),
                ('upa', models.CharField(blank=True, max_length=250, null=True)),
                ('con', models.CharField(blank=True, max_length=250, null=True)),
                ('like', models.SmallIntegerField(blank=True, null=True)),
                ('iye', models.SmallIntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('id_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flowers.categoriya')),
            ],
        ),
        migrations.CreateModel(
            name='FlowersDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fowers', models.JSONField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaSayts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SizeFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
                ('id_categoriya', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flowers.categoriya')),
            ],
        ),
        migrations.CreateModel(
            name='SeoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('id_seo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.seocategory')),
            ],
        ),
        migrations.CreateModel(
            name='FlowersImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='flowers/')),
                ('id_flowers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flowers', to='flowers.flowers')),
            ],
        ),
        migrations.CreateModel(
            name='FlowersCommentVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ImageField(blank=True, null=True, upload_to='commit/')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('id_flowers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commit', to='flowers.flowers')),
            ],
        ),
        migrations.AddField(
            model_name='flowers',
            name='id_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flowers.subcategoriya'),
        ),
    ]
