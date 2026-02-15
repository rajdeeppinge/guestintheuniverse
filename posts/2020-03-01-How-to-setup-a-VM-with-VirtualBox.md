---
layout: post
title: "How to setup a VM with VirtualBox"
date: 2020-03-01
---

###  Intro

For many IT professionals and computer scientists, it is often a requirement to test infrastructure setup, test software or tool on a small scale, or as a proof of concept for demonstrating certain ideas. In such scenarios, a virtual machine (VM) comes in handy.   


###  What is a Virtual Machine?

A virtual machine mimics an actual server in every sense but it does not require separate hardware. It can be set up on an existing physical server and uses the host hardware. It is configured to work as an isolated server without disturbing the physical server/host machine on which it runs. In simple words, the virtual machine does not know that it is a virtual machine or that it is hosted on another physical server. A user using a VM also won't be able to know if the machine is virtual or physical.   


### 

###  How to set up a VM?

There are many ways to create a VM. Virtualbox is the easiest of them all as it is easy to setup and allows us to a VM even on a laptop. So let's go ahead and create a VM using Virtualbox.  


### 

### 

###  Creating a Virtual Machine using Virtualbox

####  Install Virtualbox

Install VirtualBox from the [official website](https://www.virtualbox.org/wiki/Downloads) or from the package manager in your system like apt, brew, yum, etc.  


####  Operating System

Now we need a copy of an Operating System that is to be installed on the VM. For the purposes of this post, we'll be using the [ Ubuntu desktop ISO image](https://ubuntu.com/download/desktop) (Ubuntu 18.04 at the time of writing), however, one can choose [Ubuntu server ISO image](https://ubuntu.com/download/server) (Ubuntu without GUI) or any other Windows, Linux or Unix based OS image.  


####  Create VM

Now let's create a VM  


  1. Open Virtualbox and click on the "New" button at the top. 

  


[![](/images/Screen+Shot+2020-03-01+at+3.54.01+PM.png)]  
  
 
  2. Enter the name of VM, storage and OS details:  
  


[![](/images/Screen+Shot+2020-03-01+at+3.57.32+PM.png)]

  3. Select Memory to be allocated to VM  
\- The default is 1024 MB (1 GB). If you are not sure about memory requirements, keep it default.  
 
  4. Select existing or create a new virtual hard disk for the VM.  
\- Create a new disk if you don't have one.
  5. Choose virtual hard disk file type:  
\- Use Virtualbox Disk Image (VDI) as the virtual hard disk file type. This is the most common type used with VirtualBox VMs.   
\- There are two more types namely Virtual Hard Disk (VHD) and Virtual Machine Disk (VMDK) available but those are out of the scope of this post.
  6. Storage of virtual hard disk on the physical hard disk  
\- Make it dynamically allocated so that it doesn't unnecessarily take space on disk unless you have a very specific requirement.
  7. Specify the location of the virtual hard disk file and it's size.

Now you'll see your VM on the left-hand side in the main window:  
  


[![](/images/Screen+Shot+2020-03-01+at+4.17.40+PM.png)]

  


  
The setup is not complete yet. The VM still needs an OS.  


####  Install OS

  1. Select VM and click on "Settings" at the top. It will open the following window:  
  


[![](/images/Screen+Shot+2020-03-01+at+4.21.35+PM.png)]

  2. Go to the "Storage" tab. Click on the "Empty" disk option on the left and choose optical disk (OS image) by clicking the disk icon on the right. Click OK to save.  
  


[![](/images/Screen+Shot+2020-03-01+at+4.31.20+PM.png)]

  3. Setup "Networking" for the VM  
\- Go to the "Network" tab.  
\- Four separate Adapters (Network Interfaces) can be setup on this VM.  
\- Enable the first adapter, Attach to "Bridged Adapter" and select name as per the network your host system is connected to.  
\- This will create a bridge from VM to host network interface which will give internet access inside the VM.  
  


[![](/images/Screen+Shot+2020-03-01+at+4.37.10+PM.png)]

  
\- Again there are multiple interface options available but those would not be covered here.
  4.  Now start the VM by selecting it and clicking the "Start" button at the top. Make a "Normal Start" for now. This will open a UI.  
\- If the window is too small, increase the "Scale Factor" to the maximum in "Settings -> Display". This can be done while the VM is on.
  5. Now carry on with the standard OS installation:  
\- For Ubuntu preferably do a Minimal installation and use LVM storage.  
  
_Grab a cup of tea while your OS is being installed._
  6. Restart the VM after installation.

[![](/images/Screen+Shot+2020-03-01+at+5.29.52+PM.png)]

  
__

And there you go. The VM has been setup.  
  


###  Additional setup

####  Setup ssh access for the VM 

The VM is up but it is tedious to access it via GUI also it takes a lot of memory to run a GUI. It is better to setup ssh access so that the VM can be reached remotely from the host via ssh.   
  


  1. Navigate to the GUI of the VM and open the Terminal (a shell).

[![![]](/images/2020-03-01-How-to-setup-a-VM-with-VirtualBox-image1.png)]

  2. Install OpenSSH-Server on VM  
For Ubuntu, run: `sudo apt install openssh-server`
  3. Check the IP of the VM by running `ip a` or `ip addr`
  4. Open a terminal on the host machine and check ping and ssh connectivity to the VM from the host
    1. ping -c 4 <ip.of.vm>
    2. ssh <username>@<ip.of.vm>



####   

####  Setup headless and detachable start for VM

[![](/images/Screen+Shot+2020-04-25+at+2.09.01+PM.png)]

  
  
Virtualbox provides two more ways to start a VM in addition to the Normal Start.  


  * Headless Start: This method just starts the VM in the background but does not start the GUI. This saves a lot of system resources that are used in GUI. Use this start method extensively after setting up ssh access.
  * Detachable Start: This is a new feature since VirtualBox 5.0 wherein the GUI process is detached from the VM process. So even though the GUI opens when the VM is started, it can be closed and the VM will still keep running in the background.

In effect, it is a good idea to use Headless start after ssh setup and use Detachable start in case of GUI requirements. Using Normal start is highly discouraged.  
  


###  Conclusion

Virtualbox provides an easy way to setup a virtual machine in your local machine with minimal effort. It is easy to configure the required resources like RAM and disk. Virtualbox also simplifies the networking configuration for virtual machines by giving an option to connect them to the host network. Finally, the openssh-server installation allows us to connect to the VM remotely while the Headless and Detachable start options minimize the resource requirements of a full-fledged GUI.

