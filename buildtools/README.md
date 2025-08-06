To build the Docker image:

``` shell
sudo docker build -t oria-builder .
```

Then, to build the website (make sure you are at the root of the website!):

``` shell
sudo docker run -it -v $(pwd):/ori-a-website oria-builder bash
make -j5
```

(automated CI builds happen on every change to `Dockerfile`)
