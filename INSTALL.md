# <img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" alt="Docker Logo" height="75"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> Install first [Docker](https://docs.docker.com/get-docker/)

<!---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> `docker build -t 3dna .`
-->

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `xhost + 127.0.0.1`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `docker run --rm -v $PWD:$PWD -w $PWD -e DISPLAY=host.docker.internal:0 joan/3dna python -m 3dna data/plasmid_8k.fasta`

<br/>
<br/>

# <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Conda_logo.svg" alt="Conda Logo" height="50"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> Install first [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> `conda env create -f environment.yml`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `conda run -n 3dna python -m 3dna data/plasmid_8k.fasta`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `conda activate 3dna`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `python -m 3dna data/plasmid_8k.fasta`
