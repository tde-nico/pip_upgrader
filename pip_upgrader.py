import subprocess
import os

def main():
    upgrades = 0
    errors = 0
    upgraded_libs = []
    error_libs = []
    os.system("py -m pip install -U pip")
    libraries = subprocess.check_output('py -m pip list --outdated',shell=True).decode('cp1252')
    libs = libraries.split('\n')[2:-1]
    for lib in libs:
        if os.system("py -m pip install -U " + lib.split(' ')[0]):
            errors += 1
            error_libs.append(lib)
        else:
            upgrades += 1
            upgraded_libs.append(lib)
    print('\n\n\n[+] Upgraded ' + str(upgrades) + ' libraries\n')
    for lib in upgraded_libs:
        print(lib)
    if errors:
        print('\n[-] Errors on ' + str(errors) + ' libraries\n')
        for lib in error_libs:
            print(lib)
    input('\n'*5)


if __name__ == '__main__':
    main()
