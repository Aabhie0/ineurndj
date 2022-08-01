# ~~~~~
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0003_category_alter_post_options_post_edit_permission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blog'),
            preserve_default=False,),
    ]