import NIKIDB
from .NIKI_COLORS import colors


def NIKI_HELP(command):
    try:
        NIKIDB.Log.info("Help service requested abd invoked.")
        if command.lower() == "cd":
            print(colors.fg.yellow, "\n\tCD (Create Database): To create particular database.")
            print("\tFor example         : CD <DATABASE_NAME>\n", colors.reset)

        elif command.lower() == "ct":
            print(colors.fg.yellow, "\n\tCT (Create table)   : To create particular table in database.")
            print("\tFor example         : CT <TABLE_NAME> <ATTRIBUTE_NAME>\n", colors.reset)


        elif command.lower() == "dt":
            print(colors.fg.yellow, "\n\tDT (Delete table)   : To delete a particular table from database.")
            print("\tFor example         : DT <TABLE_NAME>\n", colors.reset)

        elif command.lower() == "ud":
            print(colors.fg.yellow, "\n\tUD (Use database)   : To use particular database.")
            print("\tFor example         : UD <DATABASE_NAME>\n", colors.reset)

        elif command.lower() == "sd":
            print(colors.fg.yellow, "\n\tSD (Show databases) : To list all databases.")
            print("\tFor example         : SD\n", colors.reset)

        elif command.lower() == "insert":
            print(colors.fg.yellow, "\n\tINSERT              : To insert values into table.")
            print(
                "\tFor example         : INSERT <TABLE_NAME> <KEY1:VALUE1|KEY2:VALUE2|...|KEY_N:VALUE_N>",
                colors.reset)

        elif command.lower() == "show":
            print(colors.fg.yellow, "\n\tSHOW                 : To show table data.")
            print("\tFor example        : SHOW <TABLE_NAME>   :                      ") 
            print("\tFor example        : SHOW <TABLE_NAME>   : [key1, key2, ..., KeyN] :")
            print("\tFor example        : SHOW <TABLE_NAME>   : {cond1, cond2, ..., condN} :")
            print("\tFor example        : SHOW <TABLE_NAME>   : [key1, key2, ..., KeyN] : {conditions} :\n", colors.reset)

        elif command == "all":
            print(colors.fg.lightgreen, "\n\tThis is MINI DATABASE designed and developed by NIKITA CHANDORE.",
                  colors.reset)
            print("\t" + "-" * 64)
            print(colors.fg.yellow, colors.bold, "\t* DATABASE RELATED COMMANDS *", colors.reset)
            print("\tSD (Show databases)  : To list all databases.")
            print("\tCD (Create database) : To create particular database.")
            print("\tUD (Use database)    : To use particular database.")
            print(colors.fg.yellow, colors.bold, "\t* TABLE RELATED COMMANDS *", colors.reset)
            print("\tST (Show tables)     : List all tables present in database.")
            print("\t" + "-" * 64)
            print("\tCT (Create table)    : To create particular table in database.")
            print("\tDT (Delete table)    : To Delete a specified table present in database.")
            print("\tINSERT (Insert data) : To insert data into table.")
            print(colors.reset, "\t" + "-" * 64)
            print(colors.fg.yellow, colors.bold, "\t* QUERY RELATED COMMANDS *", colors.reset)
            print(colors.fg.yellow, "\n\tSHOW                 : To show table data.")
            

        else:
            NIKIDB.Log.warning("Invalid help request.")
            print(colors.fg.red, "\n\tBAD COMMAND. Please use 'help' command for more info.\n", colors.reset)
    except Exception:
        NIKIDB.Log.warning("Exception occured while executing Help command.")

