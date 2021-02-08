# Image Downloader

© 2019 James M. Tucker, PhD (Cand.)

This module downloads images from various sites. The benefits of having the images local are primarily for research purposes.

## Image Main (images_main.py)
To run the application, you need to install a local python 3 virtual environment, using the `DSS_Editions/requirements.txt`.

Once you have created the venv, activate the source and run `images_main.py`. There are three required command line arguments.
1. resolution of image (e.g., 100)
2. IAA/PAM plate number (consult the Reed Catalogue)
3. Optional: a scroll siglum, e.g., 4Q394. If you use the optional siglum, you will need to install selenium driver `venv/bin` to run Chrome in a headless state.

## Licensing
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.