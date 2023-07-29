<h2 align="center">
  <img src=https://forthebadge.com/images/badges/made-with-python.svg height=28> 
  <img alt="Project License" src="https://img.shields.io/github/license/billyeatcookies/Biscuit?style=for-the-badge"> 
</h2>

# ProxyCat
ProxyCat is a Python CLI-based tool that allows you to validate a list of proxies and determine which ones are online and working. It supports automatic downloading of proxies from various online sources, making it easier for you to keep your proxy list up-to-date.

## Features
- Supports downloading of fresh proxies from various online sources / APIs.
- Automatically save all working proxies to a file.
- Custom logging and http request/response libraries.

## Prerequisites
- Python 3.10 or above is required to use ProxyCat.
- The only external library in use at the moment is the `requests` library. You can install this using pip:
  
```bash
pip install requests
```

## Installation
To install ProxyCat you simply have to clone the repository to your local machine.
You can do this by either doing:

```bash
git clone https://github.com/jwestern1337/ProxyCat.git
cd ProxyCat
```

or, by going to this [link](https://github.com/jwestern1337/ProxyCat/archive/refs/heads/main.zip).

## Usage
To run ProxyCat, use the following command:

```bash
python3 proxycat.py [OPTIONS]
```

ProxyCat currently supports the following arguments:
⋅⋅* `-h, --help`: Shows help message.
⋅⋅* `-f, --filename`: Text file containing proxies (ip:port) on each line (default=proxies.txt)
⋅⋅* `-t, --timeout`: Timeout duration in seconds (default=5)
⋅⋅* `-r, --retries`: Number of times to retry a proxy (default=2)
⋅⋅* `-d, --download`: Download proxies from the internet (default=False)

## Roadmap
I have quite a lot planned for ProxyCat in the future. For now here is a roadmap i have created:

```
1st update:
  The first update is going to be primarily focused on adding new featres ->
    - Add support for checking socks4/5 proxies (with username and password authentication supported).
    - Add the option to check more than one type of proxy at once (probably with an arg such as --multi).
    - Add the option to allow for a maximum number of threads to be used (probably with an arg such as --threads <x>).

2nd update:
  The second update is going to be focused on re-designing the UI ->
    - Add support for different languages.
    - Use tables to display final results in a nicer manner.

3rd update:
  The third (and possibly final major) update is going to be focused again on adding new features ->
    - Add support for several other types of auth methods for the socks4/5 proxies.
    - Add better support for HTTP/s proxies.
    - Possible add a database somehow (not sure yet).
    - Any other general optimisations or improvements.
```

## License
ProxyCat is licensed under the [MIT license](https://opensource.org/license/mit/) as will remain this way for the duration of the project.
