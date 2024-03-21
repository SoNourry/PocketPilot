# Generated by Django 4.2.9 on 2024-03-21 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_alter_budget_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurringexpense',
            name='category',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='category',
        ),
        migrations.AddField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance.budget'),
        ),
    ]
