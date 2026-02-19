---
layout: post
title: "Generate Large Files in Linux using dd"
date: 2019-01-19
---

The programming community often requires large files for stress testing programmes. For example, sometimes such files are required to check the response time of certain programme or testing request handling capacity of servers. Many times, it does not matter what the contents of the file are, however, it is often difficult to find such large files when the need arises. Linux provides us a fast, efficient way of generating such huge files through simple command line options.  
  
For the purposes of this demo, I am using Ubuntu 16.04 and 18.04 linux distros. Ubuntu provides dd command to create such huge files in a matter of seconds. A typical dd command to create a 1 GB file is given below.  
  


dd if=/dev/zero of=big_file.txt count=1024 bs=1048576 

####  parameters of dd:

  * if - input file from which the content is read
  * of - output file where the content is written
  * count - number of blocks in output file
  * bs - number of bytes in each block

The above command creates a file named **big_file.txt** of size (**count*bs**) i.e. **1024*1048576 bytes (1 KB * 1 MB = 1 GB)** and fills it with stream of null characters taken from input file /dev/zero.  
  


![/images/2019-01-19-Generate-Large-Files-in-Linux-using-dd.png](/images/2019-01-19-Generate-Large-Files-in-Linux-using-dd.png)

  
As you can see above, a file of size 1 GB has been created. The data transfer rate of 1.2 GB/s is visible.  
  
Let us check how much time it actually takes to create a 2 GB file.  


  


![/images/2019-01-19-Generate-Large-Files-in-Linux-using-dd.png](/images/2019-01-19-Generate-Large-Files-in-Linux-using-dd.png)

  
The above execution shows that it barely takes approximately 4 seconds to create a file of size 2 GB.  
  
For most of the requirements, the above specified dd commands and its variations will suffice in generating large files for your requirements.  
  


####  References:

<https://linux.die.net/man/1/dd>

