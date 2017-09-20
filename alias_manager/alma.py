#!/usr/bin/python
import os
import sys

home_dir = os.environ["HOME"]
aliases_file_path = os.path.join(home_dir, ".zshaliases")
zshrc_file_path = os.path.join(home_dir, ".zshrc")


def main():
    if len(sys.argv) <= 1:
        print_usage()
    elif "-i" in sys.argv:
        init_aliases_file()
    elif "-c" in sys.argv:
        print_current_aliases()
    elif "-r" in sys.argv and len(sys.argv) == 3:
        remove_alias(sys.argv[2])
    elif len(sys.argv) >= 3:
        create_alias(sys.argv[1], sys.argv[2], "-f" in sys.argv[3:])
    else:
        print("Not recognizable arguments {}".format(sys.argv[1:]))
        print_usage()


def init_aliases_file():
    global aliases_file_path, zshrc_file_path
    open(aliases_file_path, 'a').close()

    with open(zshrc_file_path, "a") as zshrc_file:
        zshrc_file.write("\nsource ~/.zshaliases # added by toolbox\n")


def create_alias(alias, command, force=None):
    print("create alias")
    existing_aliases = check_if_alias_exists(alias)
    if not existing_aliases or (existing_aliases and force):
        with open(aliases_file_path, "a+") as af:
            af.write('alias {}="{}"\n'.format(alias, command))
            print('Alias added {}="{}"'.format(alias, command))
    else:
        print("Alias already exists")
        for line in existing_aliases:
            print("{}={}".format(*line))


def remove_alias(alias):
    aliases = read_to_list()
    aliases_without_alias = filter(lambda x: alias != x[0], aliases)
    write_aliases_to_file(aliases_without_alias)
    if len(aliases) != len(aliases_without_alias):
        print("Removed all occurences of {}".format(alias))


def read_to_list():
    with open(aliases_file_path, "r") as af:
        aliases = map(convert_to_list, af)
    return aliases


def write_aliases_to_file(aliases):
    with open(aliases_file_path, "w") as af:
        af.writelines(map(lambda x: 'alias {}={}\n'.format(*x), aliases))


def convert_to_list(line):
    return line.lstrip("alias ").strip().split("=", 1)


def check_if_alias_exists(alias):
    return filter(lambda x: x[0] == alias, read_to_list())


def print_current_aliases():
    for line in read_to_list():
        print("{} {}".format(*line))


def print_usage():
    print("""Usage alma:
    -i - create .zshaliases and add that to zshrc
    -c - prints aliases defined in ~/.zshaliases 
    [alias] [command] - adds new alias to ~/.zshaliases
    -r [alias] - removes alias
""")
