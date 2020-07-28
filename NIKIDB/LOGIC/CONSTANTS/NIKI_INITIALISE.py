import os
from datetime import datetime

import NIKIDB
from LOGIC.CONTROLLERS.NIKI_UID_GENERATOR import NIKI_UID
from LOGIC.DATABASE_MANAGER.NIKI_DATABASE_JSON_HANDLER import NIKI_DATABASE_JSON_INFO


def NIKI_INIT():
    try:
        dbpath = "DATABASE"
        dbpath = os.path.abspath(dbpath)
        flag = os.path.isdir(dbpath)

        data_insert = dict()

        dt = str(datetime.today())
        creation_date, creation_time = dt.split()

        data_insert.update({"DB_Name": "NIKIDB"})
        data_insert.update({"DB_Creation_Time": str(creation_time)})
        data_insert.update({"DB_Creation_Date": str(creation_date)})

        if not flag:
            os.mkdir(dbpath)
            NIKI_DATABASE_JSON_INFO(NIKI_UID(), data_insert)
            NIKIDB.Log.info("DATABASE folder generated.")

        defaultdb = os.path.join(dbpath, "NIKIDB")
        flag = os.path.isdir(defaultdb)

        if not flag:
            os.mkdir(defaultdb)
            NIKIDB.Log.info("Default database NIKIDB created.")
    except Exception:
        NIKIDB.Log.warning("Exception occured while initialising project structure.")