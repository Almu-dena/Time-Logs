:: be sure to have the proper pyside2 uic on path
pyside2-uic --from-imports timelogs_form.ui > ../python/ui/timelogs_form.py

:: you actually need to replace this paths with fullpaths
:: Qt --convert doesn't support relative paths
python -m Qt --convert "C:\Users\almud\OneDrive\Desktop\PTD\scripts\timeLogs\python\ui\timelogs_form.py"
:: python -m Qt --convert ../python/ui/timelogs_form.py
