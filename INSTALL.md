# <img src="https://www.docker.com/sites/default/files/d8/styles/role_icon/public/2019-07/horizontal-logo-monochromatic-white.png?itok=SBlK2TGU" alt="Docker Logo" height="75"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> Install first [Docker](https://docs.docker.com/get-docker/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> `docker build -t 3dna .`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `docker run --rm -v $PWD:$PWD -w $PWD 3dna python Main.py`

<br/>
<br/>

# <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Conda_logo.svg" alt="Conda Logo" height="50"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> Install first [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.nicepng.com/png/full/506-5068487_open-install-png-logo.png" alt="Install" height="20"/> `conda env create -f environment.yml`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `conda run -n 3dna python Main.py`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `conda activate 3dna`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://icon-library.com/images/play-icon-white-png/play-icon-white-png-26.jpg" alt="Run" height="20"/> `python Main.py`
