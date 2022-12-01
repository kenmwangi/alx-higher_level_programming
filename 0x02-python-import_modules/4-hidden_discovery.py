#!/usr/bin/python3

import hidden_4

# this code will not run when file is imported

if __name__ == "__main__":

    # iterate on list of names in module
    for def_name in dir(hidden_4):
        if def_name[:2] != "__":
            print(def_name)
