# micro:bit Scrolling Game

[![github-license-image](https://img.shields.io/github/license/J4unty/microbit-Scrolling-Game)](LICENSE) [![github-last-commit-image](https://img.shields.io/github/last-commit/J4unty/microbit-Scrolling-Game)](https://github.com/J4unty/microbit-Scrolling-Game/commits/) [![github-followers](https://img.shields.io/github/followers/j4unty?label=Follow%20%40J4unty)](https://github.com/J4unty)

This is a game where you fly a spaceship and avoid asteroids.

![Scrolling Game Demo Picture](https://github.com/J4unty/microbit-Scrolling-Game/raw/master/images/demo_picture.png)

## Setup

Install Python 3.6+ with pip and then install the dependencies with:
```bash
pip install -r requirements.txt
```

## Compiling

To compile the source into a hex file use the compile.sh script.
```bash
./compile.sh
```
The output file is located at out/micropython.hex. Then copy this file onto your micro:bit.

If you have a micro:bit pluged into your computer, you can directly upload the code with the following command:
```bash
./compile.sh upload
```

There is also a `watch` option. If you want to automaticly compile and even deploy when saving the python file.
```bash
./compile.sh watch upload
```

## Testing

There are a few additional requirements for the unittests which have to be met, so install the requirements. And download the stub file with the following commands:
```bash
pip install -r test/requirements_additional_for_testing.txt
./test/setup.sh
```

Then to run the tests just type use the following command in the project directory:
```bash
pytest
```

## Missing Features

* New asteroid creation routine based on level.
* Endless Loop while crashing into astroids on a high level.
* (Sometimes the minifaction is broken, because it uses a variable twice inside the same function. Also don't use one char long variables, becuase it sometimes chooses them as replecement variable names. Maybe add a test funcation which checks the minified before a Compilation.) => cannot repreduce this currently. Only happens with variable with the same length as the obfuscation.
* Fix the syntax highlighting in the unittests.
* Add a launch.json to upload the code with a button press.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
