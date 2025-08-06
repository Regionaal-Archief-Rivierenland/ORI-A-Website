To build:

``` shell
sudo docker build -t oria-builder .
```

To run (make sure you are at the root of the website!):

``` shell
sudo docker run --rm -it -v $(pwd):/ori-a-website oria-builder /bin/bash
make -j5
```

(automated CI builds happen on every change to `Dockerfile`)
