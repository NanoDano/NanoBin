#!/usr/bin/python
"""
Setup Zsh config and other dotfiles
"""
from os import system

# Symlink zsh & vim config
system('rm $HOME/.zshrc')
system('rm $HOME/.vimrc')
system('ln -s $HOME/NanoBin/dotfiles/zshrc $HOME/.zshrc')
system('ln -s $HOME/NanoBin/dotfiles/vimrc $HOME/.vimrc')

# Setup template SSH config file
#system('mkdir -p $HOME/.ssh/')
#system('ln -s $HOME/NanoBin/dotfiles/ssh_config_example $HOME/.ssh/config.example')

# Clone oh-my-zsh if necessary
system('if [ ! -d "$HOME/.oh-my-zsh" ]; then git clone https://github.com/robbyrussell/oh-my-zsh $HOME/.oh-my-zsh; fi')

# Symlink local override files for zsh and vim
system('touch ${HOME}/.zshrc.local')
system('touch ${HOME}/.vimrc.local')

