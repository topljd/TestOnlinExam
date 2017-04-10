# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 10:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='\u8bfe\u7a0b\u540d')),
                ('decs', models.CharField(default='', max_length=500, verbose_name='\u8bfe\u7a0b\u8bf4\u660e')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bd5\u9898\u5217\u8868',
                'verbose_name_plural': '\u8bd5\u9898\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='PaperList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='\u8bd5\u5377\u540d')),
                ('is_allow', models.BooleanField(default=False, verbose_name='\u662f\u5426\u542f\u7528')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coures.CourseList', verbose_name='\u6240\u5c5e\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u8bd5\u5377\u5217\u8868',
                'verbose_name_plural': '\u8bd5\u5377\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionType', models.CharField(choices=[('xz', '\u9009\u62e9\u9898'), ('pd', '\u5224\u65ad\u9898'), ('zg', '\u95ee\u7b54')], default='xz', max_length=2, verbose_name='\u9898\u76ee\u7c7b\u578b')),
                ('content', models.TextField(verbose_name='\u9898\u76ee\u5185\u5bb9')),
                ('answer', models.TextField(verbose_name='\u6b63\u786e\u7b54\u6848')),
                ('choice_a', models.TextField(default='A.', verbose_name='A\u9009\u9879')),
                ('choice_b', models.TextField(default='B.', verbose_name='B\u9009\u9879')),
                ('choice_c', models.TextField(default='C.', verbose_name='C\u9009\u9879')),
                ('choice_d', models.TextField(default='D.', verbose_name='D\u9009\u9879')),
                ('score', models.IntegerField(default=0, verbose_name='\u5206\u503c')),
                ('note', models.TextField(default='\u95ee\u7b54\u9898\u5728\u6b64\u5904\u505a\u7b54', verbose_name='\u5907\u6ce8\u4fe1\u606f')),
                ('boolt', models.TextField(default='True', verbose_name='\u5224\u65ad\u6b63\u8bef\u6b63\u786e\u9009\u9879')),
                ('boolf', models.TextField(default='False', verbose_name='\u5224\u65ad\u6b63\u8bef\u9519\u8bef\u9009\u9879')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coures.CourseList', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u9898\u5e93',
                'verbose_name_plural': '\u9898\u5e93',
            },
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coures.PaperList', verbose_name='\u8bd5\u5377\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='paper',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coures.Question', verbose_name='\u9898\u76ee'),
        ),
    ]