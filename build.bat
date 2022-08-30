pip install pyinstall
pip install pipreqs
pipreqs .
pip install -r requirements.txt
@RD /S /Q "build"
@RD /S /Q "dist"
pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --name "vive la resolution" --add-binary "ChangeScreenResolution.exe;."  "vivelaresolution.py"
@RD /S /Q "build"
REN dist output
pause
