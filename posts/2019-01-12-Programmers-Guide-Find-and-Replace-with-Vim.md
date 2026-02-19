---
layout: post
title: "Programmer's Guide: Find and Replace with Vim"
date: 2019-01-12
---

Many of us don't like Vim because of it's unconventional and unique command set. But if you get to know certain functionalities common to other popular editors, you would not be required to lift your hands from keyboard while typing. One such functionality that we often use in editors is "Find and Replace". The same feature, with many more customizations, is also provided by Vim. This post will focus on various Find and Replace features of Vim.  
  
Let's start with a file which contains a lot of "lorem ipsum".  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

  
Now let us replace "lorem ipsum" with "hello world".  
  
First, we will focus on replacing "lorem" with "hello" in the first line. We need to execute following command in vim.  


:s/lorem/hello/g 

  
The **:s** signifies "substitute" command provided by vim.  
The **g** flag at the end means "global". This means that all the occurrences in the selected context will be changed. In this case, all the occurrences in the first line will be changed.  
  
In the below image, you can see "lorem" has been replace by "hello" in the first line.  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

  
  
Let us now replace all the "lorem" with "hello". To replace all, we use **:%s** instead of **:s**.  
Command:  


:%s/lorem/hello/g 

  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

  
If you observe closel, the "Lorem" in the second line has not been replaced. This is because, by default, the substitute function is case-sensitive. We need to use **i** flag to make it case-insensitive.  
Command:  


:%s/lorem/hello/gi 

  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

  
But Find and Replace (F&R) tools also ask for confirmation before actually making changes. Can we do that in vim? Yes of course! Vim can do everything that a normal F&R tool can do. Just use **c** flag at the end. Let us replace all the "ipsum" with "world".  
Command:  


:%s/ipsum/world/gc 

  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

Here,  
y: yes, replace this match  
n: no, skip this match  
a: all, replace all  
q: quit  
l: last match i.e.replace this match and exit  
The last two are just to scroll up or down.  
  
So, after pressing **a** , we have accomplished our objective of replacing "lorem ipsum" with "hello world".  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

  
Finally, when we want to replace exactly matching words and not all the matches, for example, in the above file if we want to replace "is" with "was" but do not want to replace the substring "**is** " in "Th**is** ", we can use the following command:  


:%s/\&#60is\&#62/was/gc 

  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

  


![/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png](/images/2019-01-12-Programmers-Guide-Find-and-Replace-with-Vim.png)

  
There are many more uses of Vim ":substitute" command. I hope this post will encourage you to explore more about them. I would recommend using command line and Vim to work with files on remote servers.

