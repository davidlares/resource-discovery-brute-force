# davidDiscover

davidDiscover is a basic tool that simulates force brute attacks using a custom TXT dictionary that checks the URI, and other related content of HTTP resources on an specific target. This also takes screenshots for returning `200 OK` statuses in order to automate and simplify Resource Discovery elements on a web application pentesting process.

Selenium works as an automation tool for testing, which triggers the `ChromeDriver` software that display a headless `Chromium Browser` instance for taking a screen capture of the current evaluated site/uri combo.

## WAPP (Web Application Pentesting Process): Vulnerability Discovery

  1. Common Tools:

  - `Dictionary attacks`: list of known words in order to identify resource
  - `Bruce forcing`: list of combinations of string (identity resource)
  - `Fuzzing`: resource discovery

  What we can find: file directories, actions, servlets, parameters or anything HTTP accesible

## Virtualenv

In order to isolate this whole working environment, I recommend using a Virtualenv instance with the Python 2.7

For linux: (assuming you have the virtualenv library installed)

`virtualenv -p /usr/bin/python [any name]`

Then, you should activate the environment.

## Script and arguments

The working name for this project is `davidBrute` because my lackness of creativity for naming stuff. For executing the code, you'll have to:

`python fb.py` where you:

  - `-c`: excluding any particular HTTP status code
  - `-d`: dictionary usage
  - `-t`: number of threads (for non-blocking operations)
  - `-w`: target URL: (you must include the /WORD -> this is the start point for the dictionary injection)

Example:

`python fb.py -t 5 -w https://encarguelo.com/WORD -d dictionaries/custom_dictionary -c 404`

## Credits

  - [David Lares](https://twitter.com/davidlares3)

## License

  - [MIT](https://opensource.org/licenses/MIT)
