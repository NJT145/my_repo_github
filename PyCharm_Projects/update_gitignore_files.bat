@setlocal

@for /F "delims=" %%I in ("%~dp0.") do @set myRoot=%%~fI

@cmd /C  "gi python > %myRoot%\py2\.gitignore"
@cmd /C  "echo Pipfile.lock >> %myRoot%\py2\.gitignore"
@cmd /C  "echo .venv >> %myRoot%\py2\.gitignore"

@cmd /C  "gi python > %myRoot%\py3\.gitignore"
@cmd /C  "echo Pipfile.lock >> %myRoot%\py3\.gitignore"
@cmd /C  "echo .venv >> %myRoot%\py3\.gitignore"

@cmd /C  "gi python > %myRoot%\excelCompareColumns\.gitignore"
@cmd /C  "echo Pipfile.lock >> %myRoot%\excelCompareColumns\.gitignore"
@cmd /C  "echo .venv >> %myRoot%\excelCompareColumns\.gitignore"

@cmd /C  "gi python > %myRoot%\ResizeNSaveImageToBTM\.gitignore"
@cmd /C  "echo Pipfile.lock >> %myRoot%\ResizeNSaveImageToBTM\.gitignore"
@cmd /C  "echo .venv >> %myRoot%\ResizeNSaveImageToBTM\.gitignore"

@endlocal
