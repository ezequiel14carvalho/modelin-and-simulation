Project setup
-------------

Python virtual environment and dependencies for this project.

Windows (PowerShell):

```powershell
# create venv
python -m venv .venv
# activate
.\.venv\Scripts\Activate.ps1
# upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows (cmd):

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

VS Code: select the interpreter from `.venv` (Command Palette → Python: Select Interpreter).
