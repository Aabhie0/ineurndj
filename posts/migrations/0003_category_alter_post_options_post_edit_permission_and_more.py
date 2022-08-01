# ~~~

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created_at',)},
        ),
        migrations.AddField(
            model_name='post',
            name='edit_permission',
            field=models.IntegerField(choices=[(0, 'Anyone can edit '), (1, 'Only you and admin can edit')], default=1),
        ),
        
        
        
        
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(default='uncategorized', to='posts.Category'),
        ),
    ]