# Environment Setup

Creating virtual environment :
```
conda create --name fast_env
```

Activate the virtual environment :

```
conda activate fast_env
conda install --file requirements.txt
conda install -n fast_env uvicorn
conda install -c conda-forge fastapi
conda install -c anaconda pymongo

```

Run the docker-compose : `docker-compose up -d` <br>
Start the web server :
```
uvicorn main:app --host localhost --port 7108
or just run dev.sh
```
Deactivate the virtual environment : `deactivate` <br>
List all running localstack services : `localstack status services`

Swagger docs : http://localhost:9501/docs
