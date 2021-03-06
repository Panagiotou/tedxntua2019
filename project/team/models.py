from django.db import models
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

class TeamMember(models.Model):
    '''Model for members of the TEDxNTUA 2019 organizing team.

    The `team` attribute is represented as a CharField with limited possible
    values. The definition follows the official documentation example:
    https://docs.djangoproject.com/en/2.1/ref/models/fields/#choices
    '''
    EXPERIENCE = 'XP'
    IT = 'IT'
    FUNDRAISING = 'FR'
    GRAPHICS = 'GR'
    MEDIA = 'MD'
    SPEAKERS = 'SP'
    VENUE_PRODUCTION = 'VP'
    TEAM_CHOICES = (
        (EXPERIENCE, 'Experience'),
        (IT, 'IT'),
        (FUNDRAISING, 'Fundraising'),
        (GRAPHICS, 'Graphics'),
        (MEDIA, 'Media'),
        (SPEAKERS, 'Speakers'),
        (VENUE_PRODUCTION, 'Venue & Production'),
    )

    first = models.CharField(max_length=255, verbose_name='First name')
    last = models.CharField(max_length=255, verbose_name='Last name')
    email = models.EmailField()
    team = models.CharField(max_length=2, choices=TEAM_CHOICES)

    image = VersatileImageField(
        'Image',
        upload_to='static/',
        width_field='image_width',
        height_field='image_height'
    )
    image_height = models.PositiveIntegerField(editable=False, null=True)
    image_width = models.PositiveIntegerField(editable=False, null=True)

    @property
    def fullname(self):
        '''Fullname is not stored in the database, but is instead a "computed"
        value derived from the first and last attributes.
        The @property decorator in Python classes enables us to access the value
        like a normal property (e.g. `print(member.fullname)`).
        '''
        return ' '.join([self.first, self.last])

    def __str__(self):
        '''Objects of the TeamMember class are represented as strings by
        their fullname property
        '''
        return self.fullname

@receiver(models.signals.post_save, sender=TeamMember)
def WarmTeamMemberImages(sender, instance, **kwargs):
    '''Ensures images are created post-save.
    Image sizes are stored in base.VERSATILEIMAGEFIELD_RENDITION_KEY_SETS.
    Using a thumbnail__AxA rendition key, the image fits in a AxA rectangle by
    maintaining the aspect ratio.

    Documentation link:
    https://django-versatileimagefield.readthedocs.io/en/latest/overview.html#create-images-wherever-you-need-them
    '''


    img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='Sizes',
        image_attr='image',
        verbose=True
    )
    num_created, failed_to_create = img_warmer.warm()
