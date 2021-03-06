# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=40, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('sex', models.CharField(max_length=2, null=True)),
            ],
            options={
                'db_table': 'superdba_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbInfo',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('database_id', models.SmallIntegerField()),
                ('single_name', models.CharField(max_length=128, unique=True)),
                ('db_url', models.CharField(max_length=50)),
                ('dbip', models.CharField(max_length=20)),
                ('dbport', models.IntegerField()),
                ('db_user', models.CharField(max_length=40)),
                ('db_user_pwd', models.CharField(max_length=256)),
                ('db_version', models.CharField(max_length=128)),
                ('db_role', models.CharField(max_length=40)),
                ('mysql_parent_id', models.SmallIntegerField(blank=True, null=True)),
                ('db_scenario', models.CharField(max_length=8)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('descs', models.CharField(max_length=255)),
                ('project_id', models.SmallIntegerField()),
                ('gmt_create', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'db_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=100)),
                ('is_root', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('namespace', models.CharField(max_length=100)),
                ('viewname', models.CharField(max_length=100)),
                ('kwargs', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('url_name', models.CharField(max_length=100)),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 'superdba_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='mysqlfab_detail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('master_id', models.IntegerField(blank=True, null=True)),
                ('sql', models.TextField(blank=True)),
                ('descs', models.CharField(max_length=900)),
                ('gmt_create', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mysqlcheck_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='mysqlfab_master',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('db_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('username', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=100)),
                ('self_project', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('project', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=30)),
                ('gmt_create', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mysqlcheck_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PermissionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'superdba_permissionlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'superdba_rolelist',
                'managed': False,
            },
        ),
    ]
