# Research article finder

Article Finder is a simple productivity tool for readers of scientific literature. 
Article Finder takes a textual reference, determines the research article that best matches it and opens that article's web page
in a new browser tab. By using Article Finder, you can avoid copy-pasting references to Google or academic search engines
 and save a few seconds every time you are trying to locate an article online. 
 The reference can be almost anything, including the article's title, DOI number, abstract,
 list of authors and/or the journal's name, issue and page numbers.
 Article Finder is especially useful when dealing with older PDF articles whose bibliographies do not contain hyperlinks. 
 Internally, the script calls the [CrossRef API](https://www.crossref.org/services/metadata-delivery/rest-api/), which
  does the heavy lifting.
  
  
## System requirements

The program supports only Microsoft Windows at the moment. Please open a new issue if you are interested in using the tool on Linux or MacOS.

## Usage in three simple steps

1) Copy a piece of text containing the reference to clipboard with **Ctrl+c**.
2) Launch Article Finder by pressing **Ctrl+Alt+c** (the default shortcut).
3) Check that the found article looks correct.

## Installation

There are two ways to set up Article Finder on your computer. The easy way is to download and run the Windows installer. You can also use the 
Python script directly especially if you want to modify the source code yourself.

### Method 1: Pre-packaged installer

There is a ready-made 
[Windows installer](https://github.com/Jomiri/article-finder/releases/download/v1.0/ArticleFinderInstaller.exe) available on the releases page. As a standard user, you can
install Article Finder without Admin privileges if you choose your own user directory as the install location (as opposed to C:\Program
 Files, for instance). The installer automatically binds the keyboard shortcut **Ctrl+Alt+c** to Article Finder's Start menu item to make launching the tool
 as convenient as possible. If you wish to use a different hotkey combination, you can bind it to the desktop shortcut.
 
### Method 2: Python script

If you want to avoid installing anything or you want to modify to source code, you can use the script *article_finder.py* directly.
Your system must have Python 3 and the required dependencies, 
[requests](http://docs.python-requests.org/en/master/) and [pywin32](https://github.com/mhammond/pywin32), installed.
For ease of use, I recommend creating a desktop shortcut with a hotkey to the script file as explained for example
[here](https://fieldguide.gizmodo.com/create-your-own-keyboard-shortcuts-to-do-anything-on-wi-1821529700).
 
### Note concerning the CrossRef API:

 The [CrossRef API etiquette](https://github.com/CrossRef/rest-api-doc#etiquette) states that polite users of the API should
  provide a means of contacting them by including their email address in the HTTP request headers. The script
   defaults to an email address of the script's author. You do not need to change it as long as you use the script in the intended way
   by launching one search at a time.
   However, if you modify the script or start using it programmatically to send HTTP requests at a faster rate, please
   add your own email address to the *config.json* file so that the API maintainers can contact you, should your program 
   misbehave.



## Odds of success
Article Finder may sometimes find a wrong article or no article at all. 
The more complete the supplied reference is, the higher is the chance of finding the correct article.

## Compiling the executable

If you want to compile the Python script to an EXE file yourself, I recommend using [PyInstaller](https://www.pyinstaller.org/).
After cloning or downloading this project and installing PyInstaller in your environment, simply run:

 ```pyinstaller --noconsole --add-data "config.json;." article_finder.py```
 
 To package PyInstaller's output into the final installer, I used [Inno Setup](http://www.jrsoftware.org/isinfo.php),
  which I can also highly recommend.