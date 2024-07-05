# Generated by Django 5.0.6 on 2024-05-16 17:32

import accounts.enums
import django_choices_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0018_alter_clientgroupobjectpermission_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientprofile",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="clientprofile",
            name="gender",
            field=django_choices_field.fields.TextChoicesField(
                choices=[("male", "Male"), ("female", "Female"), ("nonbinary", "Non-binary")],
                choices_enum=accounts.enums.GenderEnum,
                default="female",
                max_length=9,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clientprofile",
            name="preferred_language",
            field=django_choices_field.fields.TextChoicesField(
                choices=[("english", "English"), ("spanish", "Spanish")],
                choices_enum=accounts.enums.LanguageEnum,
                default="english",
                max_length=7,
            ),
            preserve_default=False,
        ),
    ]