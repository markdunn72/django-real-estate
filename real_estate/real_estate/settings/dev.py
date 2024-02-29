from real_estate.settings.base import *

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# # EMAIL_HOST = env("EMAIL_HOST")
# # EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# # EMAIL_PORT = env("EMAIL_PORT")
# # EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
#
# EMAIL_HOST = "sandbox.smtp.mailtrap.io"
# EMAIL_HOST_USER = "e6a2e6f8defaf9"
# EMAIL_HOST_PASSWORD = "5cc7dfb3b41583"
# EMAIL_PORT = "2525"

DEFAULT_FROM_EMAIL = "info@real-estate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Real Estate"
