cd DizzWord
python -m venv venv
source ./venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init

#aqui se exporta fijando ya la api del backend
API_URL=https://dizzword.up.railway.app reflex export --frontend-only

rm -rf public

#aqui es asi porque se va a ejecutar en ubuntu
unzip frontend.zip -d public

rm frontend.zip
deactivate