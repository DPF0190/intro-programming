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
    with open(dbPath, "a") as myfile:
        myfile.write(taskString)


new_task= parseArguments(sys.argv)
save_task = (new_task)

print(sys.argv[1: ])
print(" ".join(save_task))


