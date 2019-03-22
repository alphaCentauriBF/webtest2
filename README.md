# 模拟实战项目

这个项目用来模拟使用github协作开发的过程。请各位同学对号入座，完成自己的任务。
因为Github各种小技巧很多，我不可能讲得面面俱到，希望同学们能自主学习，遇到问题的时候也可以一起讨论。
下面是关于Git和Github的教程
* [Git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/) - 重点理解分支以及仓库等的概念，不想看也可以先放下，不过建议先进行学习。
* [某视频教程](https://www.bilibili.com/video/av34406290?from=search&seid=2690806862014865878) - 以需求驱动的一个教学视频，通过这个视频可以了解一些基本的用法，建议看一下。
* [github中文非官方使用文档](https://github.com/alphaCentauriBF/github) - 一个Github使用教程，想系统学习或者遇到问题时可以查阅。
* [官方文档的一个翻译版本](http://120.79.23.183/github-xiang-dao.html) - 我翻译的。

## 起步

在开始之前，考虑到某些同学没看过上面的教程，这里给出对我们使用Github过程中常使用到的名词的解释。
#### issue
Github的用户可以在项目的issue中提出对程序的建议，Bug的报告等。可以利用issue进行需求管理，BUG追踪，交流探讨等。
#### fork
fork的意思是从别人的代码库中复制一份到你自己的代码库，与普通的复制不同，fork包含了原有库中的所有提交记录，fork后这个代码库是完全独立的，属于你自己，你可以在自己的库中做任何修改，也可以通过Pull Request向原来的库提交合并请求。
#### star
Star类似于点赞，表达你对这个项目的赞赏。
#### Pull request
Pull request也就是合并请求，当我们从某个地方获取一个程序的副本并进行修改后，如果你想将这个修改合并到你获取的程序的，就需要使用Pull request。
#### respository
github中存放文件的仓库，仓库中的文件可以受到git的管理。
#### 基本工作流
基本的工作流就是某个人发起一个项目，创建一个respository，然后其他人fork一个副本，修改后提交pull request与其合并，就达到了协作开发的效果。

### 程序的使用以及说明
* [本项目来源](https://github.com/greyli/albumy) - github上的一个项目。



### 安装

如果想运行这个项目的同学可以使用pycharm打开，本项目使用pipenv管理依赖，在2018.2以后的版本中pycharm支持pipenv。
测试环境使用python3.7
在terminal(pycharm下方的终端)输入以下命令
如果对python不熟悉实在无法进行的同学可以跳过这一部分，直接修改代码，先学会使用github

使用pipenv安装依赖
```
pipenv install --dev 
```

在本地5000端口开启web服务
```
flask run
```



## 测试
因为我给项目中的一些代码做了注释的处理，在最初的版本中所有的测试都不会通过

```
flask test
```



### 关于测试部分的说明

每个测试对应一个同学的代码。
在这里我模拟了实际开发中先编写测试再实现功能的方法(相对应的也有先实现功能再测试)，只要测试通过就可以提交代码。

```
test_index_page (test_admin.AdminTestCase) ... FAIL
test_login_normal_user (test_auth.AuthTestCase) ... ERROR FAIL
test_404_error (test_basic.BasicTestCase) ... FAIL
test_forge_command_with_count (test_cli.CLITestCase) ... FAIL
test_initdb_command (test_cli.CLITestCase) ... FAIL

在最初的版本中，所有的测试都是失败的
```
第一个测试是对于小黑负责的代码部分的测试，路径在albumy\albumy\blueprints\admin.py 的23行处，将注释去掉测试即可成功
第二个测试是对于蓝铭慧负责的代码部分的测试，路径在albumy\albumy\blueprints\auth.py 的25处开始，将注释去掉测试即可成功
第三个测试是对于张宇昊负责部分代码的测试，路径在albumy\albumy\/__init/__.py 93行处，去掉注释测试即可成功
第四个测试是对于韦家恒负责部分代码的测试，路径在albumy\albumy\/__init/__.py 132行处，去掉注释测试即可成功
第五个测试是对于张佳承负责部分代码的测试，路径在albumy\albumy\/__init/__.py 的109行处，去掉注释测试即可成功



## 任务
我们每个人要做的就是，复制一个程序副本，然后找到自己对应的部分，将注释去掉，再提交pull request合并分支，模拟协作开发的过程。下面我将给出一个参考，知只是一种可行的方式而已，各位同学可以选择自己喜欢的方式。

## 项目背景

本项目是一个图文网站，假设冯桂璠是项目的发起者，在这里创建了一个仓库，然后你们都与冯桂璠进行协作开发，在代码中注释的部分假装是没有实现的功能，我们每个人都负责其中的一部分，为了方便我们直接把注释去掉即可直接运行。下面假装我是小黑，我使用pycharm与github desktop。
### fork项目
首先，我在* [项目地址](https://github.com/alphaCentauriBF/webtest2)
处找到项目，然后点击右上角的fork按钮，然后点击右上角的头像下拉框中的your respository可以找到刚才fork的仓库
在绿色的clone or download按钮中可以将其下载到本地（需要注意的是，下载的时候请选择当前的分区为dev，在branch中可以切换当前分支），然后即可下载文件到本地并进行修改。
### 可能出现的问题
在实际开发中，你fork的项目不会随着原项目的改变而改变，当两个项目产生偏差的时候，你可以直接将自己的删除再重新获取，或者通过pull request的方式将自己fork的仓库进行更新。具体的步骤是在自己的仓库中点击项目的pull request
会看到以下的提示
Pull requests help you collaborate on code with other people. As pull requests are created, they’ll appear here in a searchable and filterable list. To get started, you should create a pull request.
点击 create a pull request.
后会进入一个页面，可能会有下述的提示
There isn’t anything to compare.
alphaCentauriBF:master is up to date with all commits from RAINLFF:master. Try switching the base for your comparison.
代表你的代码已经与代码源有了偏差，点击switching the base即可将自己的代码进行更新(原理就是通过pull request向自己的仓库发起合并请求，将新代码合并到自己的仓库中)
然后一路确定即可将自己的代码更新。

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

