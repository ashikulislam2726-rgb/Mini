# Mini — Termux AI Coding Assistant

Mini is a lightweight AI coding assistant for Termux.

## Features

- Gemma 4 26B A4B free as the primary OpenRouter model
- Automatic fallback to `openrouter/free` when the primary free provider is busy
- API key is requested at launch and is not stored in the package
- No Python third-party package is required by Mini itself
- Simple CLI UI

## Install from the public APT repository

This repository contains a small APT repository under `repo/`. It is served directly from GitHub's raw file host, so GitHub Pages is not required.

Run:

```bash
mkdir -p $PREFIX/etc/apt/sources.list.d
printf '%s\n' 'deb [trusted=yes] https://raw.githubusercontent.com/ashikulislam2726-rgb/Mini/main/repo termux main' > $PREFIX/etc/apt/sources.list.d/mini.list
pkg update
pkg install mini
```

Then:

```bash
mini
```

The package asks for the OpenRouter API key at launch and does not store the key.

## Run from source

```bash
python3 mini.py
```

## Local package build

If you are building directly in Termux:

```bash
pkg install termux-create-package termux-apt-repo -y
pip install ruamel.yaml
termux-create-package manifest.yml
apt install ./mini_1.0.0_all.deb
```
