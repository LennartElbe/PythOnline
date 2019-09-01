## Summary
The aim of this project is to compare how python scripts are run clientside
using Skulpt and in a serverside Docker container.

## Integration into ILIAS

The Ilias web-server installation uses php (v5.6). We can use this capability
to start one python job inside a docker container for each python script 
the student evaluates. After each call, the output is returned to the client
browser and the container running on the Ilias server is destroyed. This 
ensures that file changes of one user do not propagate to other users. We will
also make sure that the user permission used inside our docker container are
more restrictive so that the python scripts cannot do harm.

## How to build the Python 3.7 Docker container

The only software that the docker container needs is python (v3.7). We can 
therefore use a minimal docker image like ubuntu:18.04 to provide the python
libraries required for all student scripts.

The documentation on how to build the docker container is in 'Dockerfile'. 
Build a local version of the container with:

```
docker build -t python37 -f Dockerfile .
```
After the build your python37 docker images should be about 125mb.

## Debug instructions
In order to be able to test this project without Ilias you can start a php-based
webserver on your laptop or workstation:
```
php -S localhost:8000
```

Connect to
```
http://localhost:8000
```
and you should see a test page that includes the application. Enter a python
script on the left and press the "Compute" button. The resulting text should
appear on the right.
