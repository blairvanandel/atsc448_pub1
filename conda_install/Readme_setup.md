# To install from these files

1.  Install miniconda
1.  Launch anaconda terminal (windows)
1.  conda update -c defaults -n base conda   (to get the current conda)
1.  conda install git
1.  mkdir repos
1.  cd repos
1.  conda clone https://github.com/phaustin/a301_code.git
1.  cd a301_code\conda_install
1.  conda env create -f windows_fiona_pyarrow.yaml
1.  conda activate a448
1.  cd  ..  # (to get to a301_code)
1.  pip install -e .   # to get a301 installed into the a448 environment

(I had to hit return a couple of times to wake up the window and continue
the install, you should see a progress bar increment for each package)



