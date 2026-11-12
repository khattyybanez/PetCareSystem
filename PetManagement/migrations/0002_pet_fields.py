from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PetManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.CharField(
                choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown')],
                default='Unknown',
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name='pet',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pet',
            name='owner_contact',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='date_registered',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
