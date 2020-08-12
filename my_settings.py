DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weplash',
        'USER': 'root',
        'PASSWORD': 'soojung24',
        'HOST': 'wecode-project.chyjriz6bwsb.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS' : {
            'charset' : 'utf8mb4',
        }
    }
}

SECRET_KEY = '=+s$b(z7_5w#6otr_!ctwp8+ljy)mx^-1u0@d8cg^ve3yngq*8'
ALGORITHM = 'HS256'

EMAIL = {
     'EMAIL_BACKEND'         : 'django.core.mail.backends.smtp.EmailBackend',
     'EMAIL_HOST'            : 'smtp.gmail.com',
     'EMAIL_PORT'            : 587,
     'EMAIL_HOST_USER'       : 'minho.lee0716@gmail.com',
     'EMAIL_HOST_PASSWORD'   : 'Lmessi10@',
     'EMAIL_USE_TLS'         : True,
     'REDIRECT_PAGE'         : '',
     'SERVER_EMAIL'          : 'minho.lee0716'
}

AWS_S3= {
    'access_key'        : "AKIAUG4MBEMSMZHFF3N2",
    'secret_access_key' : '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',
    'url'               : "https://s3.ap-northeast-2.amazonaws.com/weplash/"
}

S3_URL = "https://s3.ap-northeast-2.amazonaws.com/weplash/"

IMAGGA = {
    'api_key' : 'acc_a9cffd66450632e',
    'api_secret' : '13e825f7d12ce0b22a54f89efbe21ebc'
}