---
layout: post
title: "True or False with Bash"
date: 2018-12-02
---

One of the first rules that is taught in any programming course is that 0 means False and anything that is non-zero is considered True.  
  
But when you come to system programming in Unix environment, you need to completely forget this basic programming rule. In unix shells, this rule is flipped and 0 means true / success while anything non-zero means false / failure. Every executed command in unix shells returns an exit status according to this convention.   
  
Let's see some examples in bash  
We will use the `**echo $?**` to get the exit status for the previously executed command. (The detailed explanation of this command is out of the scope of this article)  
  
The first example is as always to print "Hello World!"  


![/images/2018-12-02-True-or-False-with-Bash.png](/images/2018-12-02-True-or-False-with-Bash.png)

There are two ways of printing "Hello World!" as shown above. In both the cases, the exit status is 0 as the printing is successful.  
  
Let's check the true and false variables.  


![/images/2018-12-02-True-or-False-with-Bash.png](/images/2018-12-02-True-or-False-with-Bash.png)

  
As you can see, false returns 1.  
  
Another example using conditionals.  


![/images/2018-12-02-True-or-False-with-Bash.png](/images/2018-12-02-True-or-False-with-Bash.png)

  
We know that **true** returns 0. When it is used along with **if condition** , that condition becomes true and it prints the message in the if part.  
When **false** is used in **if condition** , the condition becomes false and the execution goes in else part.  
Notice that **"!" is the negation sign** and **! false** becomes **true**.  
  
Finally, as we have stated earlier, the non-zero values are considered as failure. This can be used to categorize different types of failures. Application developers can customize the exit status codes as per their application requirements. For example, a three step failure notification could have the following exit status assignment.  
1: Info  
2: Warning  
3: Error  


![/images/2018-12-02-True-or-False-with-Bash.png](/images/2018-12-02-True-or-False-with-Bash.png)

In the above example, observe that we are initially in bash shell. We spawn a Bourne shell (sh). Exit that shell with a status code of 3 to come back to the original bash shell. We check the status of the previous command and observe that the **sh** command i.e. the last process created by the bash shell has **exited with status code 3** meaning there is **error**.  
  
Now let me resolve that error :p   
  
  
  
  
  
  
  
  


  


