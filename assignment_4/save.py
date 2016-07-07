import os
import sys

def parseArguments(argvArray):
    """ Since sys.argv includes the name of the script itself, we omit
    the first element and combine the rest into a single string. Then we
    add a newline so appended tasks won't be bunched up."""
    all_but_command_arg = argvArray[1:]
    argsAsWord = " ".join(all_but_command_arg)
    return argsAsWord + "\n"


def saveTask(taskString):
    """ writes passed taskString to the file database"""

    dbFilename = "task_database_python.txt"
    dbPath = os.path.join( os.getenv("HOME"), dbFilename )
    print(dbPath)
    print(taskString)

task_result = parseArguments(sys.argv)

saveTask(task_result)
print(task_result)


parseArguments(sys.argv)
print(sys.argv)



