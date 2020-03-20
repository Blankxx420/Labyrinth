from cx_Freeze import setup, Executable

setup(
	 name = "MacGyver",

	 version = "0.1",

	 description = "Save Macgyver !",

	 build_exe_option = {"packages": ["os","pygame",],   
                        "include_files":["maze","player","items","constant","Images"]},

    executables =[Executable("main.py")],
)











