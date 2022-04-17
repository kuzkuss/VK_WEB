# Generated by Django 4.0.3 on 2022-04-17 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_answer_rating_question_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ratinganswer',
            unique_together={('answer', 'profile', 'grade')},
        ),
        migrations.AlterUniqueTogether(
            name='ratingquestion',
            unique_together={('question', 'profile', 'grade')},
        ),
    ]
