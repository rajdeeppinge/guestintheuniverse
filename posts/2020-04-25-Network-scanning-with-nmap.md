---
layout: post
title: "Network scanning with nmap"
date: 2020-04-25
---

nmap or network mapper is a great open-source tool for network scanning and port discovery. The detailed description of nmap is available on its [official website](https://nmap.org/). An interesting fact about nmap and its wide ranging applications from the website :p "...It was even featured in [twelve movies](https://nmap.org/movies/), including [The Matrix Reloaded](https://nmap.org/movies/#matrix), [Die Hard 4](https://nmap.org/movies/#diehard4), [Girl With the Dragon Tattoo](https://nmap.org/movies/#gwtdt), and [The Bourne Ultimatum](https://nmap.org/movies/#bourne)."  
  
Hoping that this has generated enough curiosity in you, lets focus on the very basic use of nmap in network subnet scanning. Network scanning is useful to detect hosts in the network that are reachable from the server on which nmap is run. It is also useful in security auditing of the servers exposed to internet.  
  
We have a setup of 4 VMs on a local network with each having an IP address. The local network subnet is defined as 10.0.1.1/24 and the IPs in the below images verify this fact.  
  


![/images/2020-04-25-Network-scanning-with-nmap-image0.png](/images/2020-04-25-Network-scanning-with-nmap-image0.png)

![2020-04-25-Network-scanning-with-nmap-image1.png](/images/2020-04-25-Network-scanning-with-nmap-image1.png)

![/images/2020-04-25-Network-scanning-with-nmap-image2.png](/images/2020-04-25-Network-scanning-with-nmap-image2.png)

![/images/2020-04-25-Network-scanning-with-nmap-image3.png](/images/2020-04-25-Network-scanning-with-nmap-image3.png)

  
The goal is to verify that nmap is able to detect all the hosts in the local subnet 10.0.1.1/24. Execute the following command to scan the subnet:  
`nmap <subnet.ip>`  
  
It returns a list of hosts present on the subnet. nmap also performs a port scan on the live hosts and returns a list of ports that are open on those hosts.  
  


![/images/2020-04-25-Network-scanning-with-nmap-image4.png](/images/2020-04-25-Network-scanning-with-nmap-image4.png)

  
nmap scanned 256 IP addresses i.e. the whole /24 subnet and found 4 hosts. It also scanned for ports on all hosts and found port 22 open which is the standard port running ssh service.  
  
  
There are many uses for network scanning. I have used nmap for the following two cases:  


  1. To find IP addresses of servers that are dynamically assigned IP addresses by DHCP.
  2. To detect all the running servers in a legacy infrastructure of hundreds of servers.

  
In conclusion, nmap is a simple yet powerful tool to scan subnets for running servers. It is also an important tool in security auditing. It gives information about all the open ports which can make servers vulnerable to various cyber-attacks. Use it wisely and make your systems more secure.

