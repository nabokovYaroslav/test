# Generated by Django 3.2 on 2021-05-07 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('radio', 'radio'), ('checkbox', 'checkbox'), ('text', 'text')], default='radio', max_length=20)),
                ('points', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time_to_complete', models.PositiveIntegerField(default=900)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('lesson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveIntegerField(default=0)),
                ('user_started_at', models.DateTimeField(null=True)),
                ('user_finished_at', models.DateTimeField(null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTestQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.answeroption')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
                ('user_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.usertest')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test'),
        ),
        migrations.AddField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question'),
        ),
    ]
