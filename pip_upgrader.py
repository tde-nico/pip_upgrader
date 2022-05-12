import subprocess
import os

python_command = "py"

def     upgrade():
	upgrades, errors = [], []

	os.system(python_command + " -m pip install -U pip")
	libraries = subprocess.check_output(python_command + " -m pip list --outdated",shell=True).decode("cp1252")
	libs = libraries.split('\n')[2:-1]

	for lib in libs:
		if os.system(python_command + " -m pip install -U " + lib.split(' ')[0]):
			errors.append(lib)
		else:
			upgrades.append(lib)

	return upgrades, errors



def	main():
	upgrades, errors = upgrade()

	print('\n\n\n[+] Upgraded ' + str(len(upgrades)) + ' libraries\n')
	for lib in upgrades:
		print(lib)
	if errors:
		print('\n[-] Errors on ' + str(len(errors)) + ' libraries\n')
		for lib in errors:
			print(lib)
	input("\n\n")


if __name__ == '__main__':
	main()
