**intaload** is a module for downloading sets of Instagram profiles with [**instaloader**](https://github.com/instaloader/instaloader). The code is provided for informational purposes only; any usage or modification is prohibited without the copyright holder's written permission.


## Required components
1. Python (version 3.13 recommended)
2. [instaloader](https://github.com/instaloader/instaloader) module with the following PRs merged:
   * https://github.com/instaloader/instaloader/pull/2577
   * https://github.com/instaloader/instaloader/pull/2578
   * https://github.com/instaloader/instaloader/pull/2581
  Optionally, you may also merge:
   * https://github.com/instaloader/instaloader/pull/2579
3. [browser-cookie3](https://github.com/borisbabic/browser_cookie3) module
  Optionally, you may merge:
   * https://github.com/borisbabic/browser_cookie3/pull/225
   * https://github.com/borisbabic/browser_cookie3/pull/226


## Recommended installation
1. Install the latest version of Python from the [official website](https://www.python.org/downloads/) with PIP included.
2. In the system command prompt, run the following as an administrator:
   `pip install git+https://github.com/denyshon/instaloader`
   (instaloader will be installed with all the mentioned PRs merged)
3. In the system command prompt, run the following as an administrator:
   `pip install browser-cookie3`
   (browser-cookie3 will be installed without the mentioned PRs merged)
4. Download the source code file (instaload.py) into the working directory.
