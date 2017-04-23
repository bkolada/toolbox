#!/usr/bin/python
import os
import sys

home_dir = os.environ["HOME"]
aliases_file = os.path.join(home_dir, ".zshaliases")


def print_alias(line):
    print("{} {}".format(*line))


def convert_to_list(line):
    return line.lstrip("alias ").strip().split("=", 1)


def read_to_list():
    with open(aliases_file, "r") as af:
        aliases = map(convert_to_list, af)
    return aliases


def print_current_aliases():
    for i in read_to_list():
        print_alias(i)


def check_if_alias_exists(alias):
    return filter(lambda x: x[0]==alias, read_to_list())


def create_alias(alias, command, force=None):
    if not force:
        existing_aliases = check_if_alias_exists(alias)
        if existing_aliases:
            print("Alias already exists {}={}".format(*existing_aliases[0]))
        return
    with open(aliases_file, "a") as af:
        af.write('alias {}="{}"\n'.format(alias, command))


def print_usage():
    print("""
    Usage mali:
        -c - prints aliases defined in ~/.zshaliases 
        [alias] [command] - adds new alias to ~/.zshaliases
        -r [alias] - removes alias
    """)


def write_aliases_to_file(aliases):
    with open(aliases_file, "w") as af:
        af.writelines(map(lambda x: 'alias {}={}\n'.format(x[0], x[1]), aliases))


def remove_alias(alias):
    aliases = read_to_list()
    aliases_without_alias = filter(lambda x: alias != x[0], aliases)
    write_aliases_to_file(aliases_without_alias)
    if len(aliases) != len(aliases_without_alias):
        print("Removed {}".format(alias))

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