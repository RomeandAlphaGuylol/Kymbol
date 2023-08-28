import configparser
import os
print("Parsing build properties file [OK]")
BUILD = configparser.ConfigParser()

try:
    print("Reading build properties file [OK]")
    BUILD.read('build.properties')
except Exception as e:
    print(f"{e} [ERROR]")
print("Reading file path [OK]")
PATH = BUILD.get('DEFAULT', 'PATH')
try:
    print("Reading test options [OK]")
    test = BUILD.get('BUILD', 'test')
except Exception as e:
    print(f"{e} [ERROR]")

if test=="true":
    try:
        os.chdir("tests")
        print("Running tests [OK]")
        os.system("python3 test.py |> test.log")
    except Exception as e:
        print(f"{e} [ERROR]")
elif test=="false":
    print("Test option false")
    try:
        os.chdir(PATH)
        print("Running main module [OK]")
        try:
            os.system("pyinstaller --onefile main.py") # pyinstaller (https://pyinstaller.org/en/stable/ or https://pypi.org/project/pyinstaller/)
            
        except:
            os.system("pip install pyinstaller")
    except Exception as e:
        print(f"{e} [ERROR]")
else:
    print(f"Unkown value: {test}")