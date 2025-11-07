
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('MovieID', models.AutoField(primary_key=True, serialize=False)),
                ('MovieTitle', models.CharField(max_length=100)),
                ('Actor1Name', models.CharField(max_length=100)),
                ('Actor2Name', models.CharField(max_length=100)),
                ('DirectorName', models.CharField(max_length=100)),
                ('MovieGenre', models.CharField(max_length=50)),
                ('ReleaseYear', models.IntegerField()),
            ],
        ),
    ]
