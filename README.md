## davidDiscover

davidDiscover is a basic tool that simulates brute force attacks using a custom TXT dictionary that checks the URI and other related content of HTTP resources on a specific target. This also takes screenshots for returning `200 OK` statuses to automate and simplify Resource Discovery elements on a web application pentesting process.

Selenium works as an automation tool for testing, which triggers the `ChromeDriver` software that displays a headless `Chromium Browser` instance for taking a screen capture of the current evaluated site/URI combo.

![davidBrute](https://i.ibb.co/7r3QnCb/davidbrute.png "davidBrute")

## WAPP (Web Application Pentesting Process): Vulnerability Discovery

  1. Common Tools:

  - `Dictionary attacks`: a list of known words to identify the resource
  - `Bruce forcing`: list of combinations of string (identity resource)
  - `Fuzzing`: resource discovery

  What we can find: file directories, actions, servlets, parameters or anything HTTP accessible

## Virtualenv

To isolate this whole working environment, I recommend using a Virtualenv instance with Python 2.7

For Linux: (assuming you have the virtualenv library installed)

`virtualenv -p /usr/bin/python [any name]`

Then, you should activate the environment.

## Script and arguments

The working name for this project is `DavidBrute` because of my lack of creativity for naming stuff. To execute the code, you'll have to:

`python fb.py` where you:

  - `-c`: excluding any particular HTTP status code
  - `-d`: dictionary usage
  - `-t`: number of threads (for non-blocking operations)
  - `-w`: target URL: (you must include the /WORD -> this is the start point for the dictionary injection)

Example:

`python fb.py -t 5 -w https://encarguelo.com/WORD -d dictionaries/custom_dictionary -c 404`

## Credits
[David E Lares S](https://davidlares.com)

## License
[MIT](https://opensource.org/licenses/MIT)
