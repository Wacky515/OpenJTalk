# OpenJTalk
## How to install
### Linux

Execute following command

```sh
$ sudo apt install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001
$ wget https://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip/download -O MMDAgent_Example-1.6.zip
$ unzip MMDAgent_Example-1.6.zip MMDAgent_Example-1.6/Voice/*
$ sudo cp -r MMDAgent_Example-1.6/Voice/mei/ /usr/share/hts-voice
```
