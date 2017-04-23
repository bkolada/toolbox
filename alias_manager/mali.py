#!/usr/bin/python
import os
import sys

home_dir = os.environ["HOME"]
aliases_file = os.path.join(home_dir, ".zshaliases")


def print_alias(line):
    print("{} {}".format(line[0], line[1]))


def convert_to_list(line):
    return line.lstrip("alias ").strip().split("=", 1)


def read_to_list():
    with open(aliases_file, "r") as af:
        aliases = map(convert_to_list, af)
    return aliases


def print_current_aliases():
    for i in read_to_list():
        print_alias(i)


def create_alias(alias, command):
    with open(aliases_file, "a") as af:
        af.write('alias {}="{}"\n'.format(alias, command))


def print_usage():
    print("""
    Usage mali:
        -c - prints aliases defined in ~/.zshaliases 
        [alias] [command] - adds new alias to ~/.zshaliases
        -r [alias] - removes alias
    """)


def remove_alias(alias):
    pass


if __name__=="__main__":
    if len(sys.argv) <= 1:
        print_usage()
    elif "-c" in sys.argv:
        print_current_aliases()
    elif "-r" in sys.argv and len(sys.argv) == 3:
        remove_alias(sys.argv[2])
    elif len(sys.argv) == 3:
        create_alias(sys.argv[-2], sys.argv[-1])
    else:
        print("Not recognizable arguments {}".format(sys.argv[1:]))
        print_usage()