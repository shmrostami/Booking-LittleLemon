
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_alter_booking_no_of_guests"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking", name="booking_date", field=models.DateField(),
        ),
    ]
