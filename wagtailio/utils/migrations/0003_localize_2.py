# Generated by Django 2.2.12 on 2020-05-08 11:11

from django.db import migrations

from wagtail_localize.bootstrap import BootstrapTranslatableModel


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_localize_1'),
    ]

    operations = [
        BootstrapTranslatableModel('utils.LinkGroupLink'),
        BootstrapTranslatableModel('utils.LinkGroupSnippet'),
        BootstrapTranslatableModel('utils.MenuSnippet'),
        BootstrapTranslatableModel('utils.MenuSnippetLink'),
    ]