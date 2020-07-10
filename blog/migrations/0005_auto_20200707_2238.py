# Generated by Django 3.0.6 on 2020-07-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('page_view', models.IntegerField(verbose_name='ページビュー数')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_at',
        ),
        migrations.AddField(
            model_name='post',
            name='friend_posts',
            field=models.ManyToManyField(blank=True, related_name='_post_friend_posts_+', to='blog.Post', verbose_name='関連記事'),
        ),
        migrations.AddField(
            model_name='post',
            name='publish_at',
            field=models.BooleanField(default=True, null=True, verbose_name='公開可能か?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='タグ'),
        ),
    ]