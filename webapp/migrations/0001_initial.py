# Generated by Django 4.0.5 on 2022-07-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='автор')),
                ('email', models.EmailField(max_length=50, verbose_name='почта')),
                ('text', models.CharField(max_length=3000, verbose_name='текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('active', 'активная'), ('blocked', 'заблокировано')], default='active', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'гостевая книга',
                'verbose_name_plural': 'гостевые книги',
                'db_table': 'Guestbooks',
            },
        ),
    ]
