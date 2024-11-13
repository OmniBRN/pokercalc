# pokercalc

This is a poker calculator I wrote in Python.

It uses the Monte Carol Method to evaluate the cards.

# How to Run

Requirements : Python and Bash (this was not really written to be used by other people since it only runs using an input file and simple bash commands, but hopefully I can make a GUI for it to be worth the time to use)

I provided an input file, named "input", that comments and also the input needed for the script to run.

I also provided a inputscript script to strip the comments from the input since I haven't actually thought to make the input commentable when I started, and this seemed like the fastest fix.

So when the input file is finished you then run it as so: `./inputscript < input | ./pokercalc`



## Motivation

I enjoy playing poker and I don't really enjoy the services the internet provides when it comes to evaluation of poker hands. So I decided it could be fun to write my own, since it also helps me with starting a "Project" and finishing it.

I added a burned pile and fixed many bugs, and now the evaluation is pretty much identical with other websites.

## Anything Left?

Adding a GUI would be cool, depends on how I feel