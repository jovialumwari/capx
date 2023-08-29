from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=128)
    profile_image = models.URLField(max_length=256)
    profile_header = models.URLField(max_length=256)
    description = models.CharField(max_length=512)
    wiki_link = models.URLField(max_length=256)
    date_of_creation = models.DateField()
    date_of_last_edit = models.DateField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=35)


class Skill_Family(Profile):
    # empty for now
    def __str__(self):
        return self.name


class Skill(Profile):
    self_learning = models.URLField(max_length=256)
    family = models.ForeignKey(Skill_Family, null=False, on_delete=models.CASCADE)


class User_Profile(Profile):
    birthday = models.DateField()
    pronouns = models.CharField(max_length=32)
    languages = models.ForeignKey(Language, null=False, on_delete=models.CASCADE)
    email = models.EmailField(max_length=128)
    twitter = models.CharField(max_length=50)
    discord = models.CharField(max_length=50)
    skills_known = models.ForeignKey(Skill, null=True, on_delete=models.CASCADE, related_name="skills_known")
    skills_to_learn = models.ForeignKey(Skill, null=True, on_delete=models.CASCADE, related_name="skills_to_learn")


class Event(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User_Profile, null=True,
                                on_delete=models.CASCADE)  # should be linked to CapX user ID and not the profile ID
    date_of_creation = models.DateField()
    date_of_last_edit = models.DateField()
    description = models.CharField(max_length=512)
    wiki_link = models.URLField(max_length=256)
    in_person_event = models.BooleanField()
    country = models.CharField(max_length=50)