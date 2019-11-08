FIELD_IMAGE = 'image'
FIELD_VIDEO = 'video'
FIELD_PROGRAMMING = 'programming'
FIELD_MUSIC = 'music'
FIELD_PERFORMANCE = 'performance'
FIELD_OBJECT = 'object'
FIELD_IDEA = 'idea'
FIELDS = (
    (FIELD_IMAGE, 'image'),
    (FIELD_VIDEO, 'video'),
    (FIELD_PROGRAMMING, 'programming'),
    (FIELD_MUSIC, 'music'),
    (FIELD_PERFORMANCE, 'performance'),
    (FIELD_OBJECT, 'object'),
    (FIELD_IDEA, 'idea'),
)

IMAGE_BRANDING = 'branding'
IMAGE_DIGITAL_ART = 'digital_art'
IMAGE_FINE_ART = 'fine_art'
IMAGE_GRAPHIC_DESIGN = 'graphic_design'
IMAGE_ILLUSTRATION = 'illustration'
IMAGE_PHOTOGRAPHY = 'photography'
IMAGE_UI_UX = 'ui/ux'
IMAGE_TYPOGRAPHY = 'typography'
IMAGE_INTERACTION = 'interaction'
IMAGE_FIELDS = (
    (IMAGE_BRANDING, 'branding'),
    (IMAGE_DIGITAL_ART, 'digital_art'),
    (IMAGE_FINE_ART, 'fine_art'),
    (IMAGE_GRAPHIC_DESIGN, 'graphic_design'),
    (IMAGE_ILLUSTRATION, 'illustration'),
    (IMAGE_PHOTOGRAPHY, 'photography'),
    (IMAGE_UI_UX, 'ui/ux'),
    (IMAGE_TYPOGRAPHY, 'typography'),
    (IMAGE_INTERACTION, 'interaction'),
)

VIDEO_ANIMATION = 'animation'
VIDEO_FILM = 'film'
VIDEO_FIELDS = (
    (VIDEO_ANIMATION, 'animation'),
    (VIDEO_FILM, 'film'),
)

PROGRAMMING_INTERACTION = 'interaction'
PROGRAMMING_PROGRAMMING = 'programming'
PROGRAMMING_MEDIA = 'media'
PROGRAMMING_ART = 'art'
PROGRAMMING_DEVELOPER = 'developer'
PROGRAMMING_INSTALLATION = 'installation'
PROGRAMMING_FIELDS = (
    (PROGRAMMING_INTERACTION, 'interaction'),
    (PROGRAMMING_PROGRAMMING, 'programming'),
    (PROGRAMMING_MEDIA, 'media'),
    (PROGRAMMING_ART, 'art'),
    (PROGRAMMING_DEVELOPER, 'developer'),
    (PROGRAMMING_INSTALLATION, 'installation'),
)

MUSIC_MUSIC = 'music'
MUSIC_FIELDS = (
    (MUSIC_MUSIC, 'music'),
)

PERFORMANCE_DANCE = 'dance'
PERFORMANCE_INFLUENCER = 'influencer'
PERFORMANCE_MAKEUP = 'makeup'
PERFORMANCE_FIELDS = (
    (PERFORMANCE_DANCE, 'dance'),
    (PERFORMANCE_INFLUENCER, 'influencer'),
    (PERFORMANCE_MAKEUP, 'makeup'),
)

OBJECT_SCULPTING = 'sculpting'
OBJECT_FASHION = 'fashion'
OBJECT_INSTALLATION = 'installation'
OBJECT_CRAFT = 'craft'
OBJECT_JEWERLY = 'jewerly'
OBJECT_FIELDS = (
    (OBJECT_SCULPTING, 'sculpting'),
    (OBJECT_FASHION, 'fashion'),
    (OBJECT_INSTALLATION, 'installation'),
    (OBJECT_CRAFT, 'craft'),
    (OBJECT_JEWERLY, 'jewerly'),
)

IDEA_ART_DIRECTION = 'art-direction'
IDEA_JOURNALISM = 'idea-journalism'
IDEA_STORYTELLING = 'storytelling'
IDEA_FIELDS = (
    (IDEA_ART_DIRECTION, 'art-direction'),
    (IDEA_JOURNALISM, 'idea-journalism'),
    (IDEA_STORYTELLING, 'storytelling'),
)

ALL_FIELDS = IMAGE_FIELDS + VIDEO_FIELDS + PROGRAMMING_FIELDS + MUSIC_FIELDS + PERFORMANCE_FIELDS + \
             OBJECT_FIELDS + IDEA_FIELDS
