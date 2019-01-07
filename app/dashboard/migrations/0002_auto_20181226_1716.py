# Generated by Django 2.1.4 on 2018-12-26 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        ('kudos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preferred_kudos_wallet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preferred_kudos_wallet', to='kudos.Wallet'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interest',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interested', to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='coinredemptionrequest',
            name='coin_redemption',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.CoinRedemption'),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='bounty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments', to='dashboard.Bounty'),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fulfilled', to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='bounty_owner_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bounties_funded', to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='interested',
            field=models.ManyToManyField(blank=True, to='dashboard.Interest'),
        ),
        migrations.AddField(
            model_name='blockeduser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='bounty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='dashboard.Bounty'),
        ),
        migrations.AddField(
            model_name='activity',
            name='kudos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='kudos.KudosTransfer'),
        ),
        migrations.AddField(
            model_name='activity',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='dashboard.Tip'),
        ),
        migrations.AlterIndexTogether(
            name='bounty',
            index_together={('network', 'idx_status')},
        ),
    ]
