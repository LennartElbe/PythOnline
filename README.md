## Summary
The aim of this project is to compare how python scripts are run clientside
using Skulpt and in a serverside Docker container.

In order to start this project do the following
```
php -S localhost:8000
```
And connect to
http://localhost:8000
```
open
```

## How to build the Docker container

In order to build execute the following in bash
```
docker build -t phppython37 -f php_Dockerfile .
```