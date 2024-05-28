# Generated by Django 5.0.4 on 2024-05-27 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100, verbose_name='Payment ID')),
                ('order_id', models.CharField(max_length=100, verbose_name='Order ID')),
                ('signature', models.CharField(max_length=200, verbose_name='Signature')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
