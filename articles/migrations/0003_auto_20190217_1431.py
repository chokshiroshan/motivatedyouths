# Generated by Django 2.1.5 on 2019-02-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_secondhead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='secondhead',
        ),
        migrations.AddField(
            model_name='article',
            name='secondtext',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='secondtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='thirdtext',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='thirdtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
