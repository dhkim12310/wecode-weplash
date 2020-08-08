DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weplash',
        'USER': 'root',
        'PASSWORD': 'soojung24',
        'HOST': 'wecode-project.chyjriz6bwsb.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}

SECRET_KEY = '=+s$b(z7_5w#6otr_!ctwp8+ljy)mx^-1u0@d8cg^ve3yngq*8'
ALGORITHM = 'HS256'
# EMAIL = {
#      'EMAIL_BACKEND'         : 'django.core.mail.backends.smtp.EmailBackend',
#      'EMAIL_HOST'            : 'smtp.gmail.com',
#      'EMAIL_PORT'            : 587,
#      'EMAIL_HOST_USER'       : 'minho.lee0716@gmail.com',
#      'EMAIL_HOST_PASSWORD'   : 'Lmessi10@',
#      'EMAIL_USE_TLS'         : True,
#      'REDIRECT_PAGE'         : '',
#      'SERVER_EMAIL'          : 'minho.lee0716'
# }