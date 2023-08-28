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
if PATH=="" or " ":
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
            os.system("python3 main.py")
        except Exception as e:
            print(f"{e} [ERROR]")
    else:
        print(f"Unkown value: {test}")
else:
    print("build.properties: Enter a valid path! [ERROR]")