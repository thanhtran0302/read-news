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
```shell
$> scrapy crawl news -a 'url=https://www.economist.com/leaders/2021/01/16/why-a-dawn-of-technological-optimism-is-breaking'
```

### Read news
Once Scrapy has done the job. The script will generate a `article.html` file. You can open it, and enjoy your article. 

## Supported websites
* [The Economist](https://www.economist.com)
* [The Diplomat](https://thediplomat.com)
* [Foreign Policy](https://foreignpolicy.com)
* [Asia Nikkei](https://asia.nikkei.com)

More to come...

## TODO
* Possibility to pass multiples urls in parameter.
  * Generate one HTML file for each url.
* Put all generated HTMl in one directory
* Generate a `index.html` file to list all HTML files in directory
* Rename HTML file with article title.
* Provide own style of HTML, to make the reading experience better.
