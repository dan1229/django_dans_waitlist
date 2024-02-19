from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WaitlistEntry",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_modified", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "verbose_name": "Waitlist Entry",
                "verbose_name_plural": "Waitlist Entries",
                "ordering": ["email"],
            },
        ),
    ]
