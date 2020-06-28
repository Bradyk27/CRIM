import sys
from cx_Freeze import setup, Executable
exe = Executable("gamev15.py")
includefiles = ["crim.png", "map.txt", "readme.rtf", "Crim Guide.docx", "Crim Report.docx","test.mp3", "win.mp3"]
includes = []
excludes = ["tkinter"]
packages = []

setup(
    name = "CRIM",
    version = "1.5",
    description = "By Brady Kruse",
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [exe]
    )
