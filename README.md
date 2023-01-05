# pySimpleFileOrganizer
A simple, Python File organizer


A small python software I wrote out of my need to better organize my Desktop  and folders. Sometimes, when time is short and the workload doesn't allow me to, 
I tend to fill my Desktop with unsorted files. 

<h4>How it works</h4><hr>
Behind the scenes, this software will use a settings file ('settings.ini') and will read information about how you expect your files organized. It allows you to have your own rules about how to organize the files. <br>
To safely move the files I used the .replace function from the "os" library. Further implementation for unix systems may use the mv function.

<h4>How to install</h4><hr>
1. Here there are two options. You can either download the binary. It was compiled using pyinstaller and should run out of the box for any Windows device. <br><br>
2. You can also grab this repository and start it with python. Make sure to install the requirements from <code>requirements.txt</code> file! Simply start it by running <code>python main.py</code><br>
3. That's it! 

<h4>Usage</h4><hr>
As stated above, the usage is self explainatory, you will be shown a menu with 3 options.<br>
1. First option (<b>Start</b>) will run the software and will prompt you to choose the folder you want to organize. It will then parse your settings.ini file and according to that, move the files and folders in a new folder called "Backup - timestamp", where to timestamp is the current time (date - time).<br>
2. This option (<b>Customize</b>) will open the <code>settings.ini</code> file and allow you to modify and customize for your needs. Inside, you will find something like: <br>
<code>[Formats]
Music = .mp3,.wav
Documents = .txt,.rtt,.ppt
Pictures = .png,.jpg
</code><br>
You can edit this and for example add a new category. Let's say you want all of your video files to be moved in a folder called "Winter Memories", simply add it inside the Format category. Our modified file will look like this:<br>
<code>[Formats]
Music = .mp3,.wav
Documents = .txt,.rtt,.ppt
Pictures = .png,.jpg
Winter Memories = .mp4,.mkv,.avi
</code><br>
There are no limitations as to how many categories / extensions you can add. <strong> Please note that any file that does not fit into a category will simply be moved to the "others" folder.</strong>


<h4>Further work</h4><hr>
This project does what it is supposed to do, but for further developing more options can be added to simplify even more. Ideas that can be implemented, depending on your use case include: <br>
  - Folder archiving (to ease storage when backing up) <i>Here, I'd go with shutil library. It supports both zip and tar archives and allows one-line arhive creation.</i><br>
  - FTP backup of your files. So that you are sure you have an extra copy. <i>I'd use ftplib here, as it is pretty straightforward</i><br>
  - Dropbox also provides a python API that can be used to store files in the cloud.

<h4>Licensing</h4><hr>
Feel free to use this software as you wish! It is free, opensource and no credits are required if you decide to use it!
