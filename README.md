**intaload** is a module for downloading sets of Instagram profiles with [**instaloader**](https://github.com/instaloader/instaloader). The code is provided for informational purposes only; any usage or modification is prohibited without the copyright holder's written permission.


## Required components
- Python (version 3.13 recommended)
- [instaloader](https://github.com/instaloader/instaloader) module with the following PRs merged:
   * [#2577](https://github.com/instaloader/instaloader/pull/2577)
   * [#2612](https://github.com/instaloader/instaloader/pull/2612)
   * (optionally, recommended) [#2600](https://github.com/instaloader/instaloader/pull/2600)
   * (optionally) [#2579](https://github.com/instaloader/instaloader/pull/2579)
- [browser-cookie3](https://github.com/borisbabic/browser_cookie3) module with the following PRs merged:
   * (optionally) [#225](https://github.com/borisbabic/browser_cookie3/pull/225)
   * (optionally) [#226](https://github.com/borisbabic/browser_cookie3/pull/226)


## Recommended installation
1. Install the latest version of Python from the [official website](https://www.python.org/downloads/) with PIP included.
2. [Install Git](https://github.com/git-guides/install-git).
3. In the system command prompt, run the following as an administrator (instaloader will be installed with all the mentioned PRs merged, and browser-cookie3 will be installed without the mentioned PRs merged):<br/>
   ```
   pip install git+https://github.com/denyshon/instaload
   ```


## Usage
Run `instaload/src/instaload/instaload.py`.
* If you installed the module using a package manager, you can also execute
  ```
  instaloader
  ```