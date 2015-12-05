#!/bin/bash
input_fun() {
    OUTPUT_VAR=$1
    INPUT_VAR=""
    while [ -z $INPUT_VAR ];do
	read -p "$OUTPUT_VAR" INPUT_VAR
    done
    echo $INPUT_VAR
}
user_add() {
    USERNAME=$(input_fun "please input new user name:")
    useradd $USERNAME
    passwd $USERNAME
}
user_add
chmod +w /etc/sudoers
echo "$USERNAME		ALL=(ALL)	ALL" >> /etc/sudoers
chmod -w /etc/sudoers
