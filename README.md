# micro:bit Scrolling Game

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

## Missing Features

* New asteroid creation routine based on level.
* Endless Loop while crashing into astroids on a high level.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
