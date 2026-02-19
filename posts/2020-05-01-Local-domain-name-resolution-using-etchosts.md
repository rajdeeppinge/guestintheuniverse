---
layout: post
title: "Local domain name resolution using /etc/hosts"
date: 2020-05-01
---

The /etc/hosts file is a powerful mechanism for managing the information about hosts in the local network in the absence of a local DNS server.  


####  Setup

We have 4 VMs in the local /24 network. The following are the details:  
vm-1-ubuntu-16-04 - 10.0.1.11  
vm-2-ubuntu-16-04 - 10.0.1.12  
vm-1-ubuntu-18-04 - 10.0.1.21  
vm-2-ubuntu-18-04 - 10.0.1.22  
  
The VMs are reachable via their IP address but not by their hostnames.  
  


![/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png](/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png)

  
This is problematic because we have to remember their IP addresses everytime we want to access these hosts. It is would be much simpler to remember and access the servers by their hostnames. For that we need some sort of mapping between the IP addresses and their corresponding host names. There are 3 common ways of achieving this mapping.  


  1. Setup a DNS server which handles resolution for your local network.
  2. Use an existing DNS server of the local Internet Service Provider (ISP) or any other higher level ISP. Note that a public static IP address is required for this setup.
  3. Handle the name resolution on every host on the local network via the /etc/hosts file.

The first option is the best and least expensive. However, it is not always feasible to setup a local DNS server. First of all, it needs to be setup and maintained. Secondly, it may be a huge overhead for a local network containing a very small number of hosts as is our case.  
  
Since we have only 4 hosts in the network, we'll go for the third option. Let's add entries for all the hosts in the /etc/hosts file on every server.  
  


![/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png](/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png)

  
Test ping and try connecting via the hostname now.  
  


![/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png](/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png)

  


![/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png](/images/2020-05-01-Local-domain-name-resolution-using-etchosts.png)

  
And there you have it! Connected via the hostname.  


####  Use cases

  1. To identify hosts on a local network by their hostnames.
  2. For testing a production setup  
At my work, we run our company website on a public domain name. When there is a new feature development, we need to test it first in a staging environment before adding it to production. We load the updated code on a test server and update our local /etc/hosts file to point the company website URL to the IP address of the test server which is reachable from the local machine. This way the local browser resolves the website domain to the IP specified in the /etc/hosts file and we can easily test the new features.

  
Modifying the /etc/hosts file is one of the simplest ways of overriding or substituting the DNS name resolution for local network.  
  
_Have you used any innovative ways of resolving local domain names? Let me know in the comments._

