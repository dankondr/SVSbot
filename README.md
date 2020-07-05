# Dr.Sergey V.Smirnov Bot
A simple telegram bot which repeats message if it was said two times in a row.

## Dependencies

Project depends on 2 repositories:
- <a href="https://github.com/eternnoir/pyTelegramBotAPI">eternnoir/pyTelegramBotAPI</a>
- <a href="https://github.com/barseghyanartur/transliterate">barseghyanartur/transliterate</a>

## Deploy

<p align="center">
  <a href="https://docker.com/" target="_blank">
    <img src="https://i.imgur.com/SZc8JnH.png" alt="docker" />
  </a>
</p>

You can deploy SVSBot using Docker containers on Windows, macOS, and Linux distributions.

### Requirements

- [Docker](https://www.docker.com/community-edition#/download)

### Build & Run

```
docker build -t svsbot .
docker run svsbot
```
