import os
# Flask Configuration
SECRET_KEY = 'dev'
DEBUG = True

# MongoDB Configuration
# MONGO_URI = 'mongodb://root:example@localhost:27017'
MONGO_URI = 'mongodb://trustadmin:dotmail123@mongodb.youngstorage.in:27017/?authSource=trust'
MONGO_DBNAME = 'trust'

# Email Configuration
MAIL_SERVER = 'smtp.office365.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'flora63mcdaniel@outlook.com'
MAIL_PASSWORD = 'flora63@mcdaniel'
MAIL_DEFAULT_SENDER = 'flora63mcdaniel@outlook.com'

# Admin Credentials
ADMIN_USER = 'admin'
ADMIN_PASSWORD = 'admin'
SESSION_ID = 'dev'

# Image Config
UPLOAD_FOLDER = os.getcwd()+"/app/public"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
