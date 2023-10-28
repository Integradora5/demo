# demo

#crear entorno virtual
python3 -m venv .venv

#activar entorno virtual
source .venv/bin/activate

#clonar repo
git clone https://github.com/Integradora5/demo.git

#navegar al repo
cd demo

#instalar requirements
pip install -r requeriments.txt

#ejecutar proyecto
python manage.py runserver