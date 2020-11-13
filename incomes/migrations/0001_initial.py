# Generated by Django 3.0.1 on 2020-11-13 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, null=True, verbose_name='Επωνυμια')),
                ('afm', models.CharField(blank=True, max_length=10, null=True, verbose_name='ΑΦΜ')),
                ('doy', models.CharField(blank=True, default='Σπαρτη', max_length=240, null=True, verbose_name='ΔΟΥ')),
                ('notes', models.CharField(blank=True, max_length=200, verbose_name='Σημειώσεις')),
                ('cellphone', models.CharField(blank=True, max_length=20, verbose_name='Κινητό')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Τηλέφωνο')),
                ('active', models.BooleanField(default=True, verbose_name='Ενεργός')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('paid_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
            options={
                'ordering': ['title', 'afm'],
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_expired', models.DateField(verbose_name='Ημερομηνια')),
                ('title', models.CharField(blank=True, max_length=240, null=True, verbose_name='Σημειωσεις')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='ΚΑΘΑΡΗ ΑΞΙΑ')),
                ('taxes_modifier', models.CharField(choices=[('a', 0), ('b', 13), ('c', 24)], default='a', max_length=1)),
                ('taxes', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='ΦΟΡΟΣ')),
                ('order_type', models.CharField(choices=[('a', 'ΤΙΜΟΛΟΓΙΟ'), ('b', 'ΑΠΟΔΕΙΞΗ'), ('c', 'ΑΛΛΟ')], default='a', max_length=1, verbose_name='ΕΙΔΟΣ ΠΑΡΑΣΤΑΤΙΚΟΥ')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='ΑΞΙΑ')),
                ('costumer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='incomes.Costumer', verbose_name='ΠΕΛΑΤΗΣ')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.PaymentMethod', verbose_name='ΤΡΟΠΟΣ ΠΛΗΡΩΜΗΣ')),
            ],
            options={
                'ordering': ['-date_expired'],
            },
        ),
        migrations.CreateModel(
            name='CostumerPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=True, verbose_name='Πληρωμενο')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(verbose_name='Ημερομηνία')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Τίτλος')),
                ('description', models.TextField(blank=True, verbose_name='Περιγραφή')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Ποσό')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='incomes.Costumer', verbose_name='Πελάτης')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.PaymentMethod', verbose_name='Επιταγη')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
