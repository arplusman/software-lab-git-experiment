# گزارش کار آزمایش

# پاسخ پرسش‌ها

## سوال ۱

what is .git folder ?

When we initialize a new git repository , this folder is created. this folder contains all the information which git needs to have in order to manage version control in our project. 
Also we should notice that we shouldn't modify or delete anything manually in this folder and if we do that we'll have data loss. instead we should be using git commands.
if .git folder we usually have the following files :
1.config : contains configuration options for our git repository .
2.refs :contains refrences to different points in our git repository history.
3.HEAD : points to the current branch . ( or the commit we've checked out in our working directory )
4.objects :stores all the changes and files that we've commited to our hit repository.
5.hooks : contains scripts that git will run after or before certain events.

We can create .git folder both using git init and git clone commands.
By using git clone , we'll clone a copy from github.

## سوال ۲

Answer to question 2

Atomic refers to the idea of non-divisibility of an operation. when we do a atomic commit, it means that a single commit represents complete and consistent unit of change that can be applied to repository as a whole.
Thus the commit can't be broken to smaller commits and is independent from other commits made to the project. also because of the independancy of this commit ,it won't cause conflict with other commits.
About the atomic pull request, it means that this request contains a single complete and self contained unit of change that can merge to the repository without causing conflics nor breaking the code base.
It's usually connected to a single feature or bug fix and includes all the necessary coding.
The idea of "atomic" actions is to handle the changes easier without causing any conflics.

## سوال ۳

## سوال ۴

## سوال ۵

## سوال ۶
