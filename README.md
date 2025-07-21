**intaload** is a module for downloading sets of Instagram profiles with [**instaloader**](https://github.com/instaloader/instaloader). The code is provided for informational purposes only; any usage or modification is prohibited without the copyright holder's written permission.


## Required components
- Python (version 3.13 recommended)
- [instaloader](https://github.com/instaloader/instaloader) module with the following PRs merged:
   * [#2577](https://github.com/instaloader/instaloader/pull/2577)
   * [#2578](https://github.com/instaloader/instaloader/pull/2578)
   * [#2581](https://github.com/instaloader/instaloader/pull/2581)
   * (optionally) [#2579](https://github.com/instaloader/instaloader/pull/2579)
- [browser-cookie3](https://github.com/borisbabic/browser_cookie3) module with the following PRs merged:
   * (optionally) [#225](https://github.com/borisbabic/browser_cookie3/pull/225)
   * (optionally) [#226](https://github.com/borisbabic/browser_cookie3/pull/226)


## Recommended installation
1. Install the latest version of Python from the [official website](https://www.python.org/downloads/) with PIP included.
2. In the system command prompt, run the following as an administrator (to install instaloader with all the mentioned PRs merged):<br/>
   `pip install git+https://github.com/denyshon/instaloader`<br/>
3. In the system command prompt, run the following as an administrator (to install browser-cookie3 without the mentioned PRs merged):<br/>
   `pip install browser-cookie3`<br/>
4. Download the source code file (instaload.py) into the working directory.
