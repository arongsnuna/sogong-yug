# Generated by Django 4.0.4 on 2022-06-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0012_remove_post_body_post_drycleaning_post_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cloth_type',
            field=models.CharField(choices=[('Dresses', 'Dresses'), ('Blouses & Shirts', 'Blouses & Shirts'), ('Coats', 'Coats'), ('Bombers', 'Bombers'), ('T-shirts & Tops', 'T-shirts & Tops'), ('Sweatshirts', 'Sweatshirts'), ('Cardigans & Sweaters', 'Cardigans & Sweaters'), ('Jackets', 'Jackets'), ('Trousers', 'Trousers'), ('Jeans', 'Jeans'), ('Shorts', 'Shorts'), ('Skirts', 'Skirts'), ('Nightwear', 'Nightwear'), ('Underwear', 'Underwear')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='washType',
            field=models.CharField(choices=[('DO NOT WASH', 'DO NOT WASH'), ('PERMANENT PRESS', 'PERMANENT PRESS'), ('GENTLE CYCLE', 'GENTLE CYCLE'), ('HAND WASH', 'HAND WASH')], default='', max_length=20),
        ),
    ]
