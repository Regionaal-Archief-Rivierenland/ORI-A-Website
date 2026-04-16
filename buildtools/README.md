To build the Docker image:

``` shell
sudo docker build -t oria-builder .
```

Alternatively, get a pre-build image online: 

``` shell
sudo docker pull ghcr.io/regionaal-archief-rivierenland/oria-builder:latest
```

# Build the website with docker

Then, to build the website:

``` shell
cd ORI-A-Website # move to the website root
git submodule update --init # ensure you've pulled the XSD submodule (only needed once)
sudo docker run -it -v $(pwd):/ORI-A-website ghcr.io/regionaal-archief-rivierenland/oria-builder:latest bash
make -j8
```

(CI rebuilds of the image happen on every change to `Dockerfile`)
