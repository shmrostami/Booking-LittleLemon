
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking", name="no_of_guests", field=models.IntegerField(),
        ),
    ]
