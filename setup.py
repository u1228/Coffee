from cx_Freeze import setup, Executable


includefiles = ['UI/', "data/", "requirements.txt"]


options = {
    'build_exe': {
        'include_msvcr': True,
        'include_files': includefiles,
        'build_exe': 'release',

    }
}
setup(
    name="Coffee",
    version="0.0",
    description="Coffee",
    executables=[Executable("main.py", base="Win32GUI")],
    options=options
)
