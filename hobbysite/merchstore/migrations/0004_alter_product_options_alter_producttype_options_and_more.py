

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0003_product_imageurl'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering':['name']},
        ),

        migrations.RenameField(
            model_name='product',
            old_name='ImageURL',
            new_name='imageURL',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ProductType',
            new_name='productType',
        ),
        migrations.RenameField(
            model_name='producttype',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='producttype',
            old_name='Name',
            new_name='name',
        ),
    ]
