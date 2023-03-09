# گزارش کار آزمایش
در ای پروژه، پس از ساختن ریپازیتوری مورد نظر در گیت‌هاب می‌خواهیم یک پروژه‌ی ساده‌ی جنگو را توسعه دهیم. برای این کار، ابتدا با استفاده از دستور `git clone`
پروژه را کلون می‌کنیم:

<img width="726" alt="Screenshot 1401-12-17 at 1 30 44 PM" src="https://user-images.githubusercontent.com/45389988/223683720-70f5b3f3-715a-4974-9f4b-1deac49679fd.png">

پس از کلون‌کردن پروژه، یک شاخه‌ی `dev` ایحاد می‌کنیم که عملیات توسعه را در آن شاخه انجام دهیم:

<img width="733" alt="Screenshot 1401-12-17 at 3 32 51 PM" src="https://user-images.githubusercontent.com/45389988/223708515-2fe91c86-5916-42e3-8afa-8f6684d9c6dd.png">

یک محیط مجازی برای پروژه‌ی خود درست می‌کنیم تا پکیج‌های موردنیاز را در آن نصب کنیم:


<img width="731" alt="Screenshot 1401-12-17 at 3 34 58 PM" src="https://user-images.githubusercontent.com/45389988/223708919-c4687d03-c919-4ef5-a26a-838f4b404f38.png">

از آنجایی که این پکیج و برخی دیگر از فایل‌هی جنگو نباید در گیت آپلود شوند،‌ فایل
<span dir="ltr">`.gitignore`</span>
برای تعریف این فایل‌ها را ایجاد می‌کنیم. در این فایل، باید دیتابیس مورد استفاده، محیط مجازی ساخته شده و فایل‌های مربوط به تکست ادیتور و IDEها موجود باشند. سپس،‌ یک شاخه با نام
<span dir="ltr">WIP-base-config</span>
ایجاد می‌کنیم که در این شاخه تنظیمات اولیه‌ی پروژه‌ی جنگوی ما انجام می‌شود.
در این شاخه، ابتدا پروژه‌ی جنگو را در محیط مجازی ساخه‌شده ایجاد می‌کنیم:

<img width="733" alt="Screenshot 1401-12-17 at 3 46 44 PM" src="https://user-images.githubusercontent.com/45389988/223711147-a44ea908-5803-4aef-94bd-398667ae3541.png">

پس از آن، تعدادی از پکیج‌های مورد نیاز را در این محیط نصب کرده و تنظیمات متناسب با آن app را در فایل‌های پروژه انجام می‌دهیم. پس از انجام کارهای لازم، این شاخه را با با شاخه‌ی `dev` در پروژه ادغام می‌کنیم:

<img width="723" alt="Screenshot 1401-12-17 at 4 04 46 PM" src="https://user-images.githubusercontent.com/45389988/223714710-783197de-f84e-4c60-94ef-ec217928a0f8.png">

پس از ساختن بیس پروژه، قصد داریم تا یک برنامه‌ی کتابخانه‌ی آنلاین در این پروژه راه‌اندازی کنیم. برای این کار، یک شاخه با نام 
<span dir="ltr">WIP-library-app</span>
درست می‌کنیم تا توسعه‌ی این برنامه در پروژه را در این شاخه انجام دهیم. پس از توسعه‌ی برنامه، متوجه می‌شویم که روز تولید نویسنده به جای `birth_date`، `birth_data` نوشته شده‌است. برای حل این مشکل، یک شاخه با نام
<span dir="ltr">bugfix-birhtdate</span>
ایجاد میکنیم. همچنین،‌ اپ `library` در فایل تنظیمات اضافه نشده‌است. به همین دلیل یک شاخه با نام 
<span dir="ltr">bugfix-install-library-app</span>
نیز اضافه می‌کنیم. هم‌جنین در هر یک از دو شاخه تصمیم گرفته می‌شود که مقدار `max_length` برای نام و نام خانوادگی تغییر کند. که باعث ایجاد conflict در پروژه‌ی ما خواهد شد.

<img width="1680" alt="Screenshot 1401-12-18 at 4 13 02 PM" src="https://user-images.githubusercontent.com/45389988/224026413-374625be-9d25-4f2f-b543-8d5ebcd59598.png">

برای حل این conflict، فایل `models.py` را باز کرده و به کدی که می‌خواهیم نگه داریم و کدهای دیگر که با کد مربوطه تناقض دارند را پاک می‌کنیم:

<img width="1680" alt="Screenshot 1401-12-18 at 4 13 35 PM" src="https://user-images.githubusercontent.com/45389988/224026524-8e750308-d7ef-44d8-acdf-24e708ae4ec0.png">

<img width="1680" alt="Screenshot 1401-12-18 at 4 15 49 PM" src="https://user-images.githubusercontent.com/45389988/224026965-75ee624c-dd0e-4555-8d4a-db0ce71b3dff.png">

حال، فایل مورد نظر را به حال استیج برده و کامیت می‌کنیم:

<img width="702" alt="Screenshot 1401-12-18 at 4 17 39 PM" src="https://user-images.githubusercontent.com/45389988/224027367-9c01d311-9659-4e27-b303-cb456eb74a13.png">

 حال، فرض کنیم یک کانفلیت دیگر در این سیستم خواهیم داشت، ولی این بار در یک شاخه. برای این کار، فایل 
 `requirements.txt`
 را کمی تغییر می‌دهیم:
 
<img width="1234" alt="Screenshot 1401-12-18 at 4 24 11 PM" src="https://user-images.githubusercontent.com/45389988/224029169-a62e6ab1-c985-4ff0-9855-b0df59df631c.png">

هم‌چنین در کامپیوتر خود نیز در شاخه‌ی 
`dev`
ورژن این پکیج را تغییر می‌دهیم:

<img width="979" alt="Screenshot 1401-12-18 at 4 25 37 PM" src="https://user-images.githubusercontent.com/45389988/224029494-381cdcf7-d099-4d26-97d8-22ef552bdad2.png">

حال، سعی می‌کنیم تا تغییرات ایجادشده را پوش کنیم:

<img width="839" alt="Screenshot 1401-12-18 at 4 29 51 PM" src="https://user-images.githubusercontent.com/45389988/224030565-e107c982-039e-4e2d-ac9d-8c9d7208f5b7.png">

با توجه به conflict ایجاد شده، ابتدا این کانفلیکت را برطرف می‌کنیم:

<img width="1680" alt="Screenshot 1401-12-18 at 4 27 09 PM" src="https://user-images.githubusercontent.com/45389988/224029811-aef6ee2f-67cc-462b-b048-9ec082e75638.png">

<img width="504" alt="Screenshot 1401-12-18 at 4 27 55 PM" src="https://user-images.githubusercontent.com/45389988/224030003-dfbfa3ed-6609-4d17-889a-8e612d6a24eb.png">

سپس تغییرات ایجادشده را commit و بعد push می‌کنیم:

<img width="962" alt="Screenshot 1401-12-18 at 4 31 37 PM" src="https://user-images.githubusercontent.com/45389988/224031143-edc9da71-441d-46be-b705-74158fcdf5cb.png">



# پاسخ پرسش‌ها

## سوال ۱
what is .git folder ?
when we initialize a new git repository , this folder is created. this folder contains all the information which git needs to have in order to manage version control in our project. 
also we should notice that we shouldn't modify or delete anything manually in this folder and if we do that we'll have data loss. instead we should be using git commands.
if .git folder we usually have the following files :
1.config : contains configuration options for our git repository .
2.refs :contains refrences to different points in our git repository history.
3.HEAD : points to the current branch . ( or the commit we've checked out in our working directory )
4.objects :stores all the changes and files that we've commited to our hit repository.
5.hooks : contains scripts that git will run after or before certain events.

we can create .git folder both using git init and git clone commands.
by using git clone , we'll clone a copy from github.
## سوال ۲
Answer to question 2

Atomic refers to the idea of non-divisibility of an operation. when we do a atomic commit, it means that a single commit represents complete and consistent unit of change that can be applied to repository as a whole.
Thus the commit can't be broken to smaller commits and is independent from other commits made to the project. also because of the independancy of this commit ,it won't cause conflict with other commits.
About the atomic pull request, it means that this request contains a single complete and self contained unit of change that can merge to the repository without causing conflics nor breaking the code base.
It's usually connected to a single feature or bug fix and includes all the necessary coding.
The idea of "atomic" actions is to handle the changes easier without causing any conflics.
## سوال ۳
Merging refers to combining changes from one branch into another branch. when we merge two brancher , the changes made in two of them will merge together and form a new merged version of code .
 Pulling refers to downloading changes from a remote repository into our local repository and merging the change the remote one has with our local one . by pulling , we are actually updating our local version of code.
 Fetching also downloads the changes from the remote repository like pull , but unlike pull , it does'nt automatically merge the changes with our local code. thus it will only available the changes for us and we should use another command in order to merge them.
## سوال ۴

We use reverse command in order to undo a commit.
Also reset command is used for moving the branch pointer into a specified commit .
Restore command is used to restores files or directories into previous state.
Rebase is used to move the branch pointer to a new base commit.

## سوال ۵

Stage refers to the process of preparing changes to be commited into the project. when yoyu make changes to your file git will consider them initialy as unstaged. So for commiting those changes you need to stage them. by using staging you will be able to choose which changes to be in the next commit.

Stash command is used to temporarily store the changes that are not ready to be commited. it actually saves our current state of working directory on a stack of unfinished changes which is called stash.
## سوال ۶
 Each snapshot includes all of the files in our project, along with the contents of those files at the time the snapshot was taken. git uses commits to show the snapshots. it also includes some metadata such a authors , time and etc.
