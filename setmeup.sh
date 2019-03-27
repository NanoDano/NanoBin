#!/bin/bash

# Symlink zsh & vim config
ln -s $HOME/NanoBin/dotfiles/zshrc $HOME/.zshrc
ln -s $HOME/NanoBin/dotfiles/vimrc $HOME/.vimrc

# Clone oh-my-zsh if necessary
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  git clone https://github.com/robbyrussell/oh-my-zsh $HOME/.oh-my-zsh
fi

touch ${HOME}/.zshrc.local
touch ${HOME}/.vimrc.local
