#!/bin/bash

# Symlink zsh config
ln -s $HOME/NanoBin/dotfiles/zshrc $HOME/.zshrc

# Clone oh-my-zsh if necessary
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  git clone https://github.com/robbyrussell/oh-my-zsh $HOME/.oh-my-zsh
fi
