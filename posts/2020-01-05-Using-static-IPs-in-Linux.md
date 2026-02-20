---
layout: post
title: "Using static IPs in Linux"
date: 2020-01-05
---

It is often a requirement to assign static IP addresses to some important and permanent network interfaces. This is to avoid setting up a local DHCP server or relying on IP given by your network provider which may not be stable.  
  
This post shows steps to configure static IPs in Linux using Ubuntu 16.04 and Ubuntu 18.04 distros. We are considering two distros as network configuration has changed significantly in Ubuntu 18.04.  
  
There are two general steps to be followed:  
1\. Configure the network interface and assign a static IP.  
2\. Restart interface for the changes to take effect.  
  


###  Ubuntu 16.04

 The current interfaces on the system are as follows:  
  


![/images/2020-01-05-Using-static-IPs-in-Linux-image0.png](/images/2020-01-05-Using-static-IPs-in-Linux-image0.png)

  


  
As can be seen, enp0s8 interface does not have any IP. Let's assign a static IP to it. In case you already have an interface with a DHCP assigned IP, you just need to change that IP and make it static.  
  
Edit the /etc/network/interfaces file and add the following code block. Prefer using the IP address range available for private use (see [[1](https://en.wikipedia.org/wiki/Private_network)]) while deciding an IP. I want to add the server to the local 10.0.2.1/24 network. The word "static" at the end of second line indicates that this is a static IP.  
  


![/images/2020-01-05-Using-static-IPs-in-Linux-image1.png](/images/2020-01-05-Using-static-IPs-in-Linux-image1.png)

  
Now restart the network interface with the following command:  


sudo ifdown enp0s8 && sudo ip add flush dev enp0s8 && sudo ifup --force enp0s8 

  
In case this doesn't work, try restarting the networking service:  


sudo systemctl restart networking.service 

  
While this has always worked for me, in case this doesn't work, check the configuration again and restart the server:  


sudo init 6 

OR  


sudo reboot 

Upon restart the interface should be configured with static IP.  
  
This is my ifconfig output:  


![/images/2020-01-05-Using-static-IPs-in-Linux-image2.png](/images/2020-01-05-Using-static-IPs-in-Linux-image2.png)

  
Let's see how to assign a static IP for Ubuntu 18.04 before testing.  


###   

###  Ubuntu 18.04

From Ubuntu 18.04, Ubuntu shifted to Netplan network configuration. This uses yaml based configuration setup. While the method of setup changes, the steps remain the same.  
  
The current interfaces on the system are as follows:  


![/images/2020-01-05-Using-static-IPs-in-Linux-image3.png](/images/2020-01-05-Using-static-IPs-in-Linux-image3.png)

  
Here also, enp0s8 interface does not have any IP.   
  
Edit the `/etc/netplan/50-cloud-init.yaml` file (NOTE: the file name may be different depending on system) and add the following code block. Here also, we will use an IP from the 10.0.2.0/24 network. The line "dhcp4: no" indicates that this is a static IP.  
  


![/images/2020-01-05-Using-static-IPs-in-Linux-image4.png](/images/2020-01-05-Using-static-IPs-in-Linux-image4.png)

  
Apply the configuration using the following command:  


sudo netplan apply 

Use --debug flag for debugging purposes   
  


![/images/2020-01-05-Using-static-IPs-in-Linux-image5.png](/images/2020-01-05-Using-static-IPs-in-Linux-image5.png)

  
It can be seen in the above screenshot that the new config has been merged in the existing config. Let's check our interface with ifconfig,   
  


![/images/2020-01-05-Using-static-IPs-in-Linux-image6.png](/images/2020-01-05-Using-static-IPs-in-Linux-image6.png)

  
The IP has been assigned successfully.  
  


###  Testing

Make sure you are on the server which is in the same network as the network of static IPs for testing purposes. Here we will use the two servers that we have set the static IP for.  


####  PING test:

![/images/2020-01-05-Using-static-IPs-in-Linux-image7.png](/images/2020-01-05-Using-static-IPs-in-Linux-image7.png)

  


![/images/2020-01-05-Using-static-IPs-in-Linux-image8.png](/images/2020-01-05-Using-static-IPs-in-Linux-image8.png)

####  SSH test

![/images/2020-01-05-Using-static-IPs-in-Linux-image9.png](/images/2020-01-05-Using-static-IPs-in-Linux-image9.png)

  


![/images/2020-01-05-Using-static-IPs-in-Linux-image10.png](/images/2020-01-05-Using-static-IPs-in-Linux-image10.png)

####   

####  Use Cases: 

Static IPs are useful when:  


  1. The DHCP server is unstable or insufficient to manage a large number of servers. 
  2. Another possible issue is that the static IP lease expires frequently and takes time to reestablish causing frequent outages.

  
_Have you faced any such issues with your DHCP server? Have you used any innovative strategies for static IP assignment? Let me know in the comments._  
_  
_  


####  References:

####  [1] <https://en.wikipedia.org/wiki/Private_network> 

