# Generated by Django 5.0.1 on 2024-02-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_update_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=212)),
                ('last_name', models.CharField(max_length=212)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]