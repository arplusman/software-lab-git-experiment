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
درست می‌کنیم تا توسعه‌ی این برنامه در پروژه را در این شاخه انجام دهیم.

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

## سوال ۴

## سوال ۵

## سوال ۶
