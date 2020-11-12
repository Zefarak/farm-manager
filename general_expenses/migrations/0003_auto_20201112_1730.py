# Generated by Django 3.0.1 on 2020-11-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_expenses', '0002_generalexpensecategory_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalexpense',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='generalexpensecategory',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='ΑΞΙΑ'),
        ),
    ]
