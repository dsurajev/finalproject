# Generated by Django 4.0.3 on 2022-03-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_total_review_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]