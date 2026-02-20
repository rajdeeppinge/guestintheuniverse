---
layout: post
title: "Using netcat for file transfers"
date: 2019-01-20
---

Netcat is an efficient tool to transfer files between two servers in the same network. It works across all the platforms (Linux, Mac OS X and Windows). For this post, we will demo a file transfer between Ubuntu linux distro and Mac OS X.   
  
Let's first create a large file using dd tool. If you are not familiar with dd, please go through this [post](/post/2019-01-19-generate-large-files-in-linux-using-dd.md).  


![/images/2019-01-20-Using-netcat-for-file-transfers-image0.png](/images/2019-01-20-Using-netcat-for-file-transfers-image0.png)

  
Here, we have created 3 files of the same size having same content. Let us now transfer those files to Mac OS.  
  
At the receiving end, open a port using the following command:  


# For Mac systems  
nc -l [port_no] > [output_file_name]   
  
# For Linux systems  
nc -l -p [port_no] > [output_file_name] 

  


![/images/2019-01-20-Using-netcat-for-file-transfers-image1.png](/images/2019-01-20-Using-netcat-for-file-transfers-image1.png)

  
Now, run the following command from the sender side to send the file.  


nc [destination_ip] [destination_port] < [file_to_be_transferred] 

  


![/images/2019-01-20-Using-netcat-for-file-transfers-image2.png](/images/2019-01-20-Using-netcat-for-file-transfers-image2.png)

  
  


![/images/2019-01-20-Using-netcat-for-file-transfers-image3.png](/images/2019-01-20-Using-netcat-for-file-transfers-image3.png)

In the above pic, the sender machine is on the left hand side while receiver is on right. You can clearly see that the receiver has received the file of size 1 GB.  
  
Netcat is a great alternative to ssh based tools in transfering files across systems and it works for different architectures.

