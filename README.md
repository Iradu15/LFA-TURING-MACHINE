# LFA-TURING-MACHINE

# Exercise 1.

Imagine a Turing Machine (TM) that has one head and two tapes. The second tape must be a copy of the first one. Imagine the second tape as a backup copy of the first one, so it can be used to detect possible storage errors. You need to:

* Give formal definition of this type of TM.
* Give a clear explanation of computation for this type of TM. Include a formal description of computation.


You can approach the construction of this TM as a multiple-head TM or a single head TM with an interlaced tape or a single head TM with two inputs/outputs. Be creative but rigorous.

# Exercise 2. 

Implement a library/program (in a programming language of your choice) to load and validate a configuration file of a TM with one head and two tapes. Also implement a simulator for this type of TM.

# Exercise 3. 

Extend the TM simulator to validate if the two tapes are identical using as input the configuration file from previous exercise. An imme- diate approach is to compare the two tapes (arrays) which is fine, but we want an extended δ function in such a way that when then TM will reach a previous final state (as a normal TM) will proceed to check of the two tapes are identical and if so then enter to a new final state.

# Exercise 4. 

Create a configuration file for a one head, two tapes TM that recognize the language L = {w#w|where w is a string} and also check for the integrity of the tapes (if they are identical).
