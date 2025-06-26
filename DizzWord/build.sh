source ./venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init

#aqui se exporta fijando ya la api del backend
API_URL=https://dizzword.up.railway.app reflex export --frontend-only

rm -rf public
powershell -command "Expand-Archive -Path 'frontend.zip' -DestinationPath 'public'"
rm frontend.zip
deactivate