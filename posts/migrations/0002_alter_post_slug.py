# ~~~

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]
    
    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]