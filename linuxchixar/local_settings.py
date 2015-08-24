# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "r6nf_7c5k-uao1@ikqfgq-oka$oym=qakuq*=*=28+ho7pq154"
NEVERCACHE_KEY = "+t8+)x*u_2tynbz_l@v*mi5phu-08&ax6)#89%l3pq0z4*+8bn"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = ["ar.linuxchix.org", "linuxchix.com.ar"]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

FABRIC = {
    "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
    "SSH_USER": "linuxchixar",  # VPS SSH username
    "HOSTS": ["45.55.134.58"],  # The IP address of your VPS
    "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    "DB_PASS": "",  # Live database password
    "ADMIN_PASS": "",  # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
