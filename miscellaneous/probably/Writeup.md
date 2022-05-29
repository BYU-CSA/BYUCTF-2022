## Probably Writeup
Each letter has approximately a 1/4 chance of being displayed correctly. If you run the program a few times, you should be able to guess the flag based on the most common characters.

**Flag** - `byuctf{what_are_the_chances_3eep3fcs}`

## Hosting
Build with `docker build -t probably .`, run with `docker run --rm -p 40011:40000 -d --name probably probably`.