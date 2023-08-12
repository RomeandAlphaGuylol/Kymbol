import os

try:
    os.mkdir("kymbol")
    os.chdir("kymbol")
    BUILD_FILE = open("kymbol/build.properties", "w")
    BUILD_FILE.write("[DEFAULT]\nPATH=\n[BUILD]\ntest=\n#true or false")
    os.chdir("..")
    os.mkdir("tests")
    
    os.chdir("tests")
    TEST_FILE = open("test.py", "w")
    TEST_FILE.write("# write your tests here (Neither Unit test nor others, just for testing something separate)")
    os.chdir("..")
except Exception as e:
    print(f"{e} [ERROR]")