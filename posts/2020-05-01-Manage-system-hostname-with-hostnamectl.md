---
layout: post
title: "Manage system hostname with hostnamectl"
date: 2020-05-01
---

This article explains the simplest method to set hostname and Fully Qualified Domain Name (FQDN/fqdn) of any given system using hostnamectl  
  
Check that hostnamectl is present on the system by typing it in a shell. You will see output similar to the one given below.  
  


![/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image0.png](/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image0.png)

  
In case hostnamectl is not found, it is a good idea to install it.  
**sudo apt update**  
**sudo apt install systemd-services**  
  
Verify the static hostname given above using the following command:  
  


![/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image1.png](/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image1.png)

  
Also verify it by checking /etc/hostname file  
  


![/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image2.png](/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image2.png)

  
Change the hostname and set the desired hostname by running the following command and authenticating with the password.  
  
**hostnamectl set-hostname <hostname>**  
  


![2020-05-01-Manage-system-hostname-with-hostnamectl-image4.png](/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image4.png)

  
Start a new shell session or reconnect to the server to see the change in the hostname  
  


![/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image5.png](/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image5.png)

  
Again run above steps to verify that hostname has been changed correctly.  


####  Configure FQDN

While the above process may suffice to identify the host in the local network, it is not enough when the host is to be identifies uniquely over the internet.  
  
For example, here we have setup the hostname as "vm-3". However there may be many such "vm-3" on the internet. Then how to identify our "vm-3" uniquely? For that we need to also add the domain and the top-level-domain (tld), if any, of the network in which the server resides.  
  
**FQDN = [hostname].[domain].[tld]**   
  
For demo purposes, we are using domain as "shodh" and tld as "demo".  
  
Therefore, the FQDN of the demo server is _**vm-3.shodh.demo**_  
  
Let's add this FQDN to the server._****_  
  


Edit the /etc/hosts file and add FQDN in front of hostname as shown below.  
**FORMAT: <ip> <fqdn> <hostname>**  
  


![/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image6.png](/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image6.png)

  


Test the FQDN setup as follows:  
  


![/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image7.png](/images/2020-05-01-Manage-system-hostname-with-hostnamectl-image7.png)

  


That's it folks! We have successfully setup the hostname and the FQDN for our server.

