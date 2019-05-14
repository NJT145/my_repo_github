@setlocal

@for /F "delims=" %%I in ("%~dp0.") do @set myRoot=%%~fI

@cmd /C  "gi windows > %myRoot%\.gitignore"

@cmd /C  "gi codeblocks > %myRoot%\CodeBlocks_Projects\.gitignore"
@cmd /C  "gi matlab > %myRoot%\Matlab_Projects\.gitignore"

@cmd /C  "gi pycharm > %myRoot%\PyCharm_Projects\.gitignore"
@cmd /C  "gi visualstudio > %myRoot%\VisualStudio_Projects\.gitignore"

@endlocal
