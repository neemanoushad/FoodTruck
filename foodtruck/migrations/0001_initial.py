# Generated by Django 3.2.7 on 2024-03-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assigntbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=150)),
                ('food_id', models.CharField(max_length=150)),
                ('tname', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('cname', models.CharField(max_length=150)),
                ('cid', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('product_id', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='categorytbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='charitytbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=150)),
                ('c_license_no', models.CharField(max_length=150)),
                ('member', models.CharField(max_length=150)),
                ('date', models.DateField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='complainttbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=150)),
                ('msg', models.CharField(max_length=150)),
                ('reply', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='delivertbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=150)),
                ('food_id', models.CharField(max_length=150)),
                ('tname', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('cname', models.CharField(max_length=150)),
                ('cid', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='feedbacktbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=150)),
                ('feedback', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='foodreqtbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('food_name', models.CharField(max_length=150)),
                ('food_id', models.CharField(max_length=150)),
                ('date', models.DateField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('cname', models.CharField(max_length=150)),
                ('cid', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='foodtbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('food_name', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=150)),
                ('p_date', models.DateField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
                ('price', models.FloatField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(max_length=150, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userr', models.CharField(max_length=150)),
                ('product', models.CharField(max_length=150)),
                ('total_item', models.CharField(max_length=150)),
                ('total_price', models.CharField(max_length=150)),
                ('card_name', models.CharField(max_length=150)),
                ('card_number', models.FloatField(max_length=150)),
                ('cvv', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='rewardtbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=150)),
                ('uname', models.CharField(max_length=150)),
                ('point', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='trucktbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=150)),
                ('no_plate', models.CharField(max_length=150)),
                ('license_no', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='userregtbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]