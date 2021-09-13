<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img width="946" alt="Ciberseguridad" src="https://user-images.githubusercontent.com/46871300/125079966-38ef8380-e092-11eb-9b5e-8bd0314d9274.PNG">
  </a>
 
   <h3 align="center">Implementacion de SOC con herramientas Open Source</h3>

  <p align="center">
    Proporcionamos los primeros pasos a los nuevos equipos de manejo de incidentes.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explora la guia »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">Ver Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Reporta un Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Solicitar función</a>
  </p>
</p>

### Descarga los informes de Shadowserver
Script para descargar informes del servidor de sombra como archivos CSV elaborado en Python3.

La secuencia de comandos puede mantener el estado en todas las ejecuciones y descargar solo los informes nuevos.

---

```
$ ./shadowserver.py -h
usage: shadowserver.py [-h] -u USER -p PASSWORD [-s SERVER] [-k]
                       [-r READ_FILE] [-l LOG_FILE] [-D] [-d DOWNLOAD_FOLDER]

Download all reports from shadowserver

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Username
  -p PASSWORD, --password PASSWORD
                        Password
  -s SERVER, --server SERVER
                        Full URL for the reports page
  -k, --keep_state      Keep state (in "./state_file"
  -r READ_FILE, --read_file READ_FILE
                        Read this file instead of making a web request (for
                        DEBUG)
  -l LOG_FILE, --log_file LOG_FILE
                        Log to file instead of STDERR
  -D, --debug           Debug
  -d DOWNLOAD_FOLDER, --download_folder DOWNLOAD_FOLDER
                        Destination folder for CSVs - default to
                        "./shadowserver-reports"
```
