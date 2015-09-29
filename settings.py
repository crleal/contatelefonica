# Django settings for contatelefonica project.
import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOGIN_REDIRECT_URL="/"
LOGIN_URL = "/contatelefonica/login/"
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'mysql',
        'NAME': 'flptelefonia',
        'USER': 'admin',
        'PASSWORD': 'f4r3v3r',
        'HOST': '192.168.0.86',
        'PORT': '3306',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Recife'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory
# that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7nm#ek-fy&w@_qx716g$5q)o!y!5oh4-izn^#*_$f0vhe$2r$7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.csrf",
#    'cms.context_processors.media',
#    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # middleware do paginas de conteudo
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware', 
#    'cms.middleware.page.CurrentPageMiddleware',
#    'cms.middleware.user.CurrentUserMiddleware',
#    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'contatelefonica.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates"
    # or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.flatpages',     
    'django.contrib.databrowse',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'conta',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #django CMS 
#    'cms', #django CMS itself
#    'mptt', #utilities for implementing a modified pre-order traversal tree
#    'menus', #helper for model independent hierarchical website navigation
#    'south', #intelligent schema and data migrations
#    'sekizai', #for javascript and css management
#    'appmedia',
#    'cms.plugins.file',
#    'cms.plugins.flash',
#    'cms.plugins.googlemap',
#    'cms.plugins.link',
#    'cms.plugins.picture',
#    'cms.plugins.snippet',
#    'cms.plugins.teaser',
#    'cms.plugins.text',
#    'cms.plugins.video',
#    'cms.plugins.twitter',
#    'publisher',
#    'filer',
#    'cmsplugin_filer_file',
#    'cmsplugin_filer_folder',
#    'cmsplugin_filer_image',
#    'cmsplugin_filer_teaser',
#    'cmsplugin_filer_video',
#    'reversion',

)

FORMAT_MODULE_PATH='formats'
