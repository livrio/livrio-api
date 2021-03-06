import os
from pymongo import MongoClient
from bson.objectid import ObjectId


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#######################################################################
# Celery Task Broker settings.
#######################################################################


#db.accounts.createIndex( { email: 1 }, { unique: true } )
#db.isbn.createIndex( { isbn: 1, isbn_10: 1 } )
#db.books.ensureIndex({ title: "text", subtitle : "text", isbn : "text",publisher: "text",description:"text",authors:"text" })

PRODUCTION = False

if PRODUCTION:
    MONGO_PORT = 4455
    DEBUG = False
    MONGO_DB = "mongodb://db.codeway.in:4455"
    PRIMARY_ACCOUNT = ObjectId("56c088952567a539023dc419")
    rollbar.init('4a3e8a5822be413ba80214a77def3702', 'production')  # access_token, environment
else:
    MONGO_PORT = 27017
    DEBUG = True
    MONGO_DB = "mongodb://db.codeway.in:27017"
    PRIMARY_ACCOUNT = ObjectId("572fbb33a94acc3383ea1cb8")
    rollbar.init('4a3e8a5822be413ba80214a77def3702', 'production')  # access_token, environment
# Task Broker

BROKER_HEARTBEAT = 0
BROKER_URL = "amqp://livrio:trQDB8NrQrzVRBSa@queue.codeway.in:5672/livrio"
CELERY_RESULT_BACKEND = "amqp://"
CELERY_TASK_RESULT_EXPIRES = 1
CELERY_ACCEPT_CONTENT = ['pickle']
CELERYD_CONCURRENCY = 10

SLACK_HOOK = "https://hooks.slack.com/services/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"


DEBUG_CONFIG = {
    'email': 'aurelio@codeway.com.br',
    'platform': 'android',
    'token': 'drtAhphyTsw:APA91bGZHNIfXFTQfFx86poUni3CbDdyKNUbkbYvAWoURdHJF4VrQgxw7dWAnBYpjT75XPIAF4XttqLOrulccAzyGP1N-tfrbl_dM158w_fuXlrPvEUkaGK8eI8lzFOaPTWjiKQ00tX3'
}



REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

AWS = {
    'AWS_ACCESS_KEY_ID': 'AKIAIBMTRNWUF2TRMYVA',
    'AWS_SECRET_ACCESS_KEY': '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',
    'AWS_ASSOCIATE_TAG': 'livrio08-20'
}

DEFAULT = {
    'book': 'https://livrio-static.s3-sa-east-1.amazonaws.com/default/book.gif',
    'user': 'https://livrio-static.s3-sa-east-1.amazonaws.com/default/user.png',
    'cover': 'https://livrio-static.s3-sa-east-1.amazonaws.com/default/cover.jpg'
}

SENDGRID = {
    'API_KEY': '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'
}

PUSH = {
    'GCM': 'AIzaSyCbBO_cyYLTpUm3VOWx7RazZAo6kxnpoq0'
}



EVE_SETTINGS_APP = {
    'WTF_CSRF_ENABLED':True,
    'SECRET_KEY':'you-will-never-guess',
    'MONGO_HOST': 'db.codeway.in',
    'MONGO_PORT': MONGO_PORT,
    'MONGO_DBNAME': 'livrio',
    'DEBUG': True,
    #'ALLOW_UNKNOWN': True,
    'SOFT_DELETE': True,
    'SORTING': True,
    'PAGINATION': True,
    'API_VERSION': 'v1',
    'X_EXPOSE_HEADERS': ['content-type'],
    'X_HEADERS': ['x-app-platform', 'x-app-platform-lang', 'x-app-platform-version', 'x-app-version','authorization','content-type'],
    'X_DOMAINS': '*',
    'EXTRA_RESPONSE_FIELDS':[],
    'HATEOAS': False,
    'AUTH_FIELD': 'account_id',

    'OPLOG': True,
    'OPLOG_AUDIT': True,
    'IF_MATCH': False,
    'VALIDATION_ERROR_AS_STRING': True,
    'DOMAIN': {
        'accounts': {
            'cache_control': '',
            'cache_expires': 0,
            'schema': {
                'email': {
                    'type': 'string',
                    'required': True,
                    'unique': True
                },
                'fullname': {
                    'type': 'string'
                },
                'first_name': {
                    'type': 'string'
                },
                'last_name': {
                    'type': 'string'
                },
                'gender': {
                    'type': 'string'
                },
                'photo': {
                    'type': 'string'
                },
                'cover': {
                    'type': 'string'
                },
                'birthday': {
                    'type': 'string'
                },
                'origin': {
                    'type': 'dict'
                },
                'roles': {
                    'type': 'list',
                    'allowed': ['user', 'superuser', 'admin'],
                    'default': ['user']
                }
            }
        },
        'shelves': {
            'cache_control': '',
            'cache_expires': 0,
            'extra_response_fields': ['name'],
            'datasource': {
                'default_sort': [('name',1)]
            },
            'schema': {
                'name': {
                    'type': 'string',
                    'required': True
                },
                'account_id': {
                    'type':'objectid',
                    'readonly': True
                }
            }
        },
        'event_tracker': {
            'url':'tracker',
            'cache_control': '',
            'cache_expires': 0,
            'schema': {
                'type': {
                    'type': 'string',
                    'required': True
                },
                'entity_id': {
                    'type': 'string'
                },
                'origin': {
                    'type': 'dict',
                    'default' : {}
                }
            }
        }
    },
    'RESOURCE_METHODS' : ['GET','POST','DELETE'],
    'ITEM_METHODS': [ 'GET','PATCH','DELETE' ]
}

EVE_SETTINGS_ISBN = {
    'MONGO_HOST': 'db.codeway.in',
    'MONGO_PORT': MONGO_PORT,
    'MONGO_DBNAME': 'livrio',
    'DEBUG': True,
    'SOFT_DELETE': True,
    'SORTING': False,
    'PAGINATION': False,
    'API_VERSION': 'v1',
    'X_EXPOSE_HEADERS': ['content-type'],
    'X_HEADERS': ['x-app-platform', 'x-app-platform-lang', 'x-app-platform-version', 'x-app-version','authorization'],
    'X_DOMAINS': '*',
    'EXTRA_RESPONSE_FIELDS':[],
    'HATEOAS': False,
    'OPLOG': False,
    'OPLOG_AUDIT': False,
    'IF_MATCH': False,
    'VALIDATION_ERROR_AS_STRING': True,
    'DOMAIN': {
        'isbn':{
            'url':'book',
            'additional_lookup': {
                'url': 'regex("[\w\:]+")',
                'field': 'isbn',
            },
            'item_lookup_field': 'isbn',
            'cache_control': '',
            'cache_expires': 0,
            'schema': {
                'title': {
                    'type': 'string'
                },
                'subtitle': {
                    'type': 'string'
                },
                'isbn': {
                    'type': 'string',
                    'unique': True
                },
                'isbn_10': {
                    'type': 'string'
                },

                'isbn_other': {
                    'type': 'string'
                },
                'authors': {
                    'type': 'string'
                },
                'publisher': {
                    'type': 'string'
                },
                'published_date': {
                    'type': 'string'
                },
                'page_count': {
                    'type': 'string'
                },
                'categories': {
                    'type': 'list'
                },
                'language': {
                    'type': 'string'
                },
                'description': {
                    'type': 'string'
                },
                'cover': {
                    'type': 'string'
                }
            }
        }
    },
    'RESOURCE_METHODS' : ['GET','POST']
}


## MONGODB CONNECTION
mongo_client = MongoClient(MONGO_DB)
db = mongo_client.livrio
