import json
from datetime import date, datetime

from peewee import MySQLDatabase, Model
from peewee import Proxy

import VARDB

__version__ = "0.0.1"


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type %s not serializable" % type(obj))


class VARDBBase(Model):
    def __str__(self):
        return json.dumps(self._data, default=json_serial)

    def __repr__(self):
        return self.__str__()


sqldb = Proxy()
deferredEffectSetted = False


def wiredb(db):
    from VARDB.Effect import Effect
    # from VARDB.Allele import DeferredEffect
    # if not VARDB.deferredEffectSetted:
    #     DeferredEffect.set_model(Effect)
    #     VARDB.deferredEffectSetted = True
    sqldb.initialize(db)


def connect_to_db(database='vardb', user='root', password='', engine=MySQLDatabase):
    # from VARDB.Effect import Effect
    # from VARDB.Allele import DeferredEffect
    # DeferredEffect.set_model(Effect)
    mysqldb = engine(database=database, user=user, password=password)
    sqldb.initialize(mysqldb)




def connect_to_test_db():
    from peewee import SqliteDatabase
    db = SqliteDatabase(":memory:")
    sqldb.initialize(db)


def disconnect():
    VARDB.sqldb.close()


