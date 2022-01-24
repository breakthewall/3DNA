# INSTALL
## Docker
Install first [Docker](https://docs.docker.com/get-docker/)

Then, run: `docker build -t 3dna .`

## Conda
Install first [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Then, run: `conda env create -f environment.yml`

# RUN
## Docker
`docker run --rm -v $PWD:$PWD -w $PWD 3dna python Main.py`

## Conda
`conda run -n 3dna python Main.py`

or
```
conda activate 3dna
python Main.py
