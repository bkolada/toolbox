#!/bin/sh

bin_path=/usr/local/bin
toolbox_path=$HOME/.toolbox

if [ -e $toolbox_path ]
then
    while true; do
        read -p "Directory $toolbox_path exists, do you want to wipe that? [y/n] " yn
        case $yn in
            [Yy]* ) rm -rf $toolbox_path; break;;
            [Nn]* ) exit;;
            * ) echo "Please answer [y]es or [n]o.";;
        esac
    done
fi

mkdir $toolbox_path


cp -R . $HOME/.toolbox/


if [ -e $bin_path/alma ]
then
    while true; do
        read -p "File $bin_path/alma exists, do you want to replace it? [y/n] " yn
        case $yn in
            [Yy]* ) rm -f $bin_path/alma; break;;
            [Nn]* ) exit;;
            * ) echo "Please answer [y]es or [n]o.";;
        esac
    done
fi

ln -s $HOME/.toolbox/alias_manager/alma /usr/local/bin/alma

