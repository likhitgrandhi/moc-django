# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-09 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsapp', '0004_auto_20170607_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_trn_newsbookmark',
            old_name='articleId',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='tbl_trn_newsbookmark',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tbl_trn_newscomment',
            old_name='articleId',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='tbl_trn_newscomment',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tbl_trn_newslike',
            old_name='articleId',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='tbl_trn_newslike',
            old_name='userId',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='tbl_trn_newsbookmark',
            unique_together=set([('user', 'article')]),
        ),
        migrations.AlterUniqueTogether(
            name='tbl_trn_newscomment',
            unique_together=set([('user', 'article')]),
        ),
        migrations.AlterUniqueTogether(
            name='tbl_trn_newslike',
            unique_together=set([('user', 'article')]),
        ),
    ]