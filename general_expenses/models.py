from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from vendors.models import TAXES_CHOICES

CURRENCY = settings.CURRENCY


class GeneralExpenseCategory(models.Model):
    title = models.CharField(unique=True, max_length=200, verbose_name='Ονομασια')

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('generic_expenses:category_update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('generic_expenses:category_delete', kwargs={'pk': self.id})

    @staticmethod
    def filters_data(request, qs):
        search_name = request.GET.get('search_name', None)
        qs = qs.filter(title__icontains=search_name) if search_name else qs
        return qs


class GeneralExpense(models.Model):
    title = models.CharField(blank=True, max_length=200, verbose_name='ΠΕΡΙΓΡΑΦΗ')
    category = models.ForeignKey(GeneralExpenseCategory, on_delete=models.PROTECT, verbose_name='ΚΑΤΗΓΟΡΙΑ')
    value = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='ΑΞΙΑ')
    paid_value = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='ΠΛΗΡΩΤΕΟ ΠΟΣΟ')
    is_paid = models.BooleanField(default=True, verbose_name='Πληρωμενο;')
    date = models.DateField(verbose_name='ΗΜΕΡΟΜΗΝΙΑ')
    taxes_modifier = models.CharField(max_length=1, choices=TAXES_CHOICES, default='a', verbose_name='ΦΠΑ')
    total_taxes = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='ΦΟΡΟΣ')
    clean_value = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='ΚΑΘΑΡΗ ΑΞΙΑ')

    def save(self, *args, **kwargs):
        self.paid_value = self.value if self.is_paid else 0
        self.total_taxes = self.value * self.get_taxes_modifier_display()/100
        self.clean_value = self.value - self.total_taxes
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else f'Παραστατικο-{self.id}'

    def get_edit_url(self):
        return reverse('generic_expenses:update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('generic_expenses:delete', kwargs={'pk': self.id})

    def get_pay_url(self):
        return reverse('generic_expenses:pay_expense', kwargs={'pk': self.id})

    def tag_value(self):
        return f'{self.value} {CURRENCY}'

    @property
    def report_date(self):
        return self.date

    def report_expense_type(self):
        return f'Γενικα Εξοδα-{self.category.title}'

    def report_value(self):
        return self.value

    @staticmethod
    def filters_data(request, qs):
        search_name = request.GET.get('search_name', None)
        cate_name = request.GET.getlist('cate_name', None)
        qs = qs.filter(title__icontains=search_name) if search_name else qs
        qs = qs.filter(category__id__in=cate_name) if cate_name else qs
        return qs