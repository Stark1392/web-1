# Generated by Django 2.2.4 on 2020-05-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0108_auto_20200513_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='bountyfulfillment',
            name='fulfiller_identifier',
            field=models.CharField(blank=True, help_text='unique fulfiller identifier used by when payout_type is fiat', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='funder_address',
            field=models.CharField(help_text='address from which amount is deducted', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='funder_identifier',
            field=models.CharField(blank=True, help_text='unique funder identifier used by when payout_type is fiat', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='funder_profile',
            field=models.ForeignKey(help_text="funder's profile", null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='payout_type',
            field=models.CharField(blank=True, choices=[('bounties_network', 'bounties_network'), ('qr', 'qr'), ('fiat', 'fiat')], help_text='payment type used to make the payment', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='tenant',
            field=models.CharField(blank=True, choices=[('ETH', 'ETH'), ('ETC', 'ETC'), ('ZIL', 'ZIL'), ('CELO', 'CELO'), ('PYPL', 'PYPL')], help_text='specific tenant type under the payout_type', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='accepted',
            field=models.BooleanField(default=False, help_text='has the fulfillment been accepted by the funder'),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='accepted_on',
            field=models.DateTimeField(blank=True, help_text='date when the fulfillment was accepted by the funder', null=True),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='bounty',
            field=models.ForeignKey(help_text='the bounty against which the fulfillment is made', on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments', to='dashboard.Bounty'),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='fulfiller_address',
            field=models.CharField(help_text='address to which amount is credited', max_length=50),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='fulfillment_id',
            field=models.IntegerField(blank=True, help_text="bounty's fulfillment number", null=True),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='payout_amount',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='amount being paid out by funder', max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='payout_status',
            field=models.CharField(blank=True, choices=[('expired', 'expired'), ('pending', 'pending'), ('done', 'done')], help_text='payment status', max_length=10),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='payout_tx_id',
            field=models.CharField(blank=True, default='0x0', help_text='transaction id', max_length=255),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='profile',
            field=models.ForeignKey(help_text="fulfillers's profile", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fulfilled', to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='token_name',
            field=models.CharField(blank=True, help_text='token/currency in which the payout is done', max_length=10),
        ),
    ]