# **Go-Image-Parser**


### Go board image processing

This part transforms an image of a Go board to an SGF game record file.

There are 2 types of Go board images to consider:

* A screenshot of Go board from applications.
* A photo of a Go board from the real world.

It might be easy to identify all the positions of stones in a screenshot, but identifying stone positions from a real world Go board could be harder, as the stones could be improperly placed.

### Usage

Usage example (default parameters for Fox Go server):

python image_parser.py 1.png out.sgf --default_len

### Problems

**Problem**: How to deal with the black/white square (indicating the next move) from Fox Go Server?

**Problem**: How to deal with the triangle/circle indicating the current move?

### Next Steps
- [ ] Transform **screenshots** of the Go board into SGF files.