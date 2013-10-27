# -*- coding:utf-8 -*-

def cuenta_ciclistas(de=10, a=20):
    from django.db import connection, transaction
    cursor = connection.cursor()

    # Data retrieval operation - no commit required
    cursor.execute('SELECT count(*) AS cuenta FROM xbapp_ciclista WHERE (YEAR(CURDATE())-YEAR(fecha_nacimiento)) - (RIGHT(CURDATE(),5)<RIGHT(fecha_nacimiento,5))>=%s AND (YEAR(CURDATE())-YEAR(fecha_nacimiento)) - (RIGHT(CURDATE(),5)<RIGHT(fecha_nacimiento,5))<=%s', [de, a])
    row = cursor.fetchone()

    return row[0]