# pySimpleFileOrganizer
A simple, Python File organizer


A small python software I wrote out of my need to better organize my Desktop  and folders. Sometimes, when time is short and the workload doesn't allow me to, 
I tend to fill my Desktop with unsorted files. 

<h6>How it works</h6><hr>
Behind the scenes, this software will use a settings file ('settings.ini') and will read information about how you expect your files organized. It allows you to have your own rules about how to organize the files. <br>
To safely move the files I used the .replace function from the "os" library. Further implementation for unix systems may use the mv function.

