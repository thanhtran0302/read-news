# Read news

## Purpose
Read news for free. Bypass news websites with paywall

## How to use
I highly recommended using this script with a virtual environment.

After cloned this repository. Go inside this one then install `virtualenv`

### Use virtualenv
```shell
$> virtualenv .
```
After that, you should see two new directories: `bin` and `lib`

### Install dependencies
```shell
$> pip3 install -r requirements.txt
```

### Launch Scrapy

#### Single URL
```shell
$> scrapy crawl news -a 'url=https://www.economist.com/leaders/2021/01/16/why-a-dawn-of-technological-optimism-is-breaking'
```

#### Multiples URLs
```shell
$> scrapy crawl news -a 'url=https://www.economist.com/leaders/2021/01/16/why-a-dawn-of-technological-optimism-is-breaking,https://foreignpolicy.com/2021/01/14/tokyo-olympics-2020-japan-public-opinion/'
```

### Docker
Install docker on your machine.

To create the first build do:
```shell
$> docker-compose build
```

Each time you want to run the project, just do:
```shell
$> docker-compose up
```

### Read news
Once Scrapy has done the job. The script will generate a `article.html` file. You can open it, and enjoy your article. 

## Supported websites
* [The Economist](https://economist.com)
* [The Diplomat](https://thediplomat.com)
* [Foreign Policy](https://foreignpolicy.com)
* [Asia Nikkei](https://asia.nikkei.com)
* [NY Times](https://nytimes.com)
* [Le Parisien](https://www.leparisien.fr/)

More to come...

## TODO
* ~~Possibility to pass multiples urls in the parameter.~~
  * ~~Generate one HTML file for each url.~~
* ~~Put all generated HTMl in one directory~~
* Generate a `index.html` file to list all HTML files in directory
* ~~Rename HTML file with article title.~~
* Provide own style of HTML, to make the reading experience better.
