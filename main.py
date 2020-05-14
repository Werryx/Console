def kw(text):
	return("{" + text + "}")

def read(count, command="{command}"):
	f = open(".data", "r")
	unusedvarforfunctionread = f.read().split("\n")[count]
	unusedvarforfunctionread = unusedvarforfunctionread.replace("\l", "\n")
	unusedvarforfunctionread = unusedvarforfunctionread.replace(kw("command"), command)
	unusedvarforfunctionread = unusedvarforfunctionread.replace(kw("shell"), shell)
	return(unusedvarforfunctionread)
	f.close()

ID_SHELL = 0
ID_SHELL_INPUT = 1
ID_HELP = 2
ID_ERR_NOTDEFINED = 3

shell = read(ID_SHELL)
shell2 = read(ID_SHELL_INPUT)

while True:
	command = input(shell)
	if(command == "help"):
		txt_help = read(ID_HELP)
		print(txt_help)
	elif(command == "shell"):
		shell = input(shell2)
		if(shell == "reset"):
			shell = read(ID_SHELL)
		if(shell[-1] != " "):
			shell = shell + " "
	elif(command == "testshell"):
		print("Обычный shell: \"" + read(ID_SHELL) + "\"\nShell ввода: \"" + read(ID_SHELL_INPUT) + "\"")
	elif(command == "exit"):
		break
	else:
		print(read(ID_ERR_NOTDEFINED, command))
