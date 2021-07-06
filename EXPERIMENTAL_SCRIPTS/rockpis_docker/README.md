
Costruire l'immagine

```bash
$ docker build -t rockpis .
```

Verificare la porta ssh (opzionale):
```bash
$ docker port rockis 22
```

creare un bridge per `simulare` l'ip della rock:
```bash
$ docker network create --driver=bridge --subnet=192.168.4.0/24 --gateway=192.168.4.100 rock-net
```

Instanziare l'immagine:

```bash
$ docker run -d -P --name rock --net=rock-net rockpis
```

Connession all'istanza tramite ssh:

```bash
$ ssh rock@192.168.4.1
```

Se l'instanza esiste ma è interrotta (exited):
```bash
$ docker start rock
```
