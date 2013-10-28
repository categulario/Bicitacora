# -*- coding:utf-8 -*-
from django.db import connection

def cuenta_ciclistas(de=10, a=20):
    cursor = connection.cursor()

    if cursor.db.settings_dict['ENGINE'].endswith('mysql'):
        cursor.execute('SELECT count(*) AS cuenta FROM xbapp_ciclista WHERE (YEAR(CURDATE())-YEAR(fecha_nacimiento)) - (RIGHT(CURDATE(),5)<RIGHT(fecha_nacimiento,5))>=%s AND (YEAR(CURDATE())-YEAR(fecha_nacimiento)) - (RIGHT(CURDATE(),5)<RIGHT(fecha_nacimiento,5))<=%s', [de, a])

        row = cursor.fetchone()

        return row[0]
    elif cursor.db.settings_dict['ENGINE'].endswith('sqlite3'):
        cursor.execute("SELECT count(*) AS cuenta FROM xbapp_ciclista WHERE (strftime('%%Y','now')-strftime('%%Y', fecha_nacimiento)) - (strftime('%%m-%%d', 'now')<strftime('%%m-%%d', fecha_nacimiento))>=%s AND (strftime('%%Y','now')-strftime('%%Y', fecha_nacimiento)) - (strftime('%%m-%%d', 'now')<strftime('%%m-%%d', fecha_nacimiento))<=%s", [de, a])

        row = cursor.fetchone()

        return row[0]
    return 0