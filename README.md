<h1 align="center">
  ♘ Chess Analysis
</h1>

## Overview

This script allows one to analyze their most recent `chess.com` game in the style of chess.com's own _Game Review_. Free users get one _Game Review_ per day and that is kinds annoying especially if you play multiple games per day. So, I thought I could create my own since the chess engine chess.com uses, `Stockfish`, is open source and has a decent python library.

### Setup

1. Install the necessary Python modules by running `pip install req.txt`
2. Enter your username in `details.py`
3. Run `game_review.py` and begin learning
<p>&nbsp;</p>

### Optional

- **Style of Pieces**  
  The styling of the chess pieces can be changed by changing the respective files in the `pieces` folder. Simply ensure that the images have a **transparent background**, are of a **high enough resolution** (the bigger the better), have the **same file names** as the images that already exist and are in a **PNG format**.
  <p>&nbsp;</p>
- **Board Stying**  
  The styling of the board can be changed by changing the `dark_squares` and `light_squares` variables in `details.py`. Simply ensure that the colors are in a **HEX format**.
  <p>&nbsp;</p>

### Things to improve

- **Implement a Web App**  
 Bring this application to the web so that users can use it without needing to download python or the required dependencies. The easiest way to do this would be to probably use Flask but I am still looking into all the possible implementation options.
<p>&nbsp;</p>

- **~~Implement a GUI system~~**  
 I thought that I had to build a whole chess game where I could make the pieces move and then I realized I could simply take the [FEN](https://en.wikipedia.org/wiki/Fen) of each position (_FEN is an algebraic description of a chess position_) after a player moves turn that to an image, thanks to the help of a python module `fentoboardimage`, and simply display those images in sequence
<p>&nbsp;</p>

- **~~Implement a frame around the board~~**  
   This is to help people, who perhaps are just starting out at chess, to recongnize the location of the squares as the move suggestions are given in algebraic notation (_c5 for example_)

  I figured out that I could overlay the board on the frame after the board image was generated using PIL instead of trying to do it on the GUI.
  <p>&nbsp;</p>

- **Draw arrows on move suggestions**  
  Possible aesthetic improvement
  <p>&nbsp;</p>

- **Find 'great' and 'brilliant' moves**  
  These moves are phenominal moves that can be found by an engine but can be difficult to find by human players, even grandmasters.

- **Find book moves**  
These moves are moves that are commonly played in a given opening.
<p>&nbsp;</p>
