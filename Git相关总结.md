# Git概括性总结
Git小而美的解决方案，仅仅涉及四个命令：add，commit，reset，checkout
# git的三个分区：
Git 的三个分区分别是：working directory，stage/index area，commit history
分别表示：
1. 工作目录（work dir）
2. 暂存区（stage area 或 index area）
3. 提交历史（commit history）

三者之间的关系：work dir -> `git add` -> stage -> `git commit` -> commit history

# 关于commit：
我们经常说的 HEAD 或者 master 分支，都可以理解为一个指向某个 commit 的指针

# 查看状态：
* work dir 和 stage 区域的状态，可以通过命令 git status 来查看
* history 区域的提交历史可以通过 git log 命令来查看。

# 需求一：如何把 work dir 中的修改加入 stage —— `git add`
`git add`
# 需求二：如何把 stage 中的修改还原到 work dir 中——`git checkout`
先新建两个文件，然后把他们都加到 stage：
`bash
$ touch a.txt b.txt
$ git add .
$ git status`
然后我又修改了 a.txt 文件：
`bash
$ echo hello world >> a.txt
$ git status
`
现在，我后悔了，我认为不应该修改 a.txt，我想把它还原成 stage 中的空文件，怎么办？
答案是，使用 checkout 命令
`git checkout a.txt`

如果 work dir 中被修改的文件很多，可以使用通配符全部恢复成 stage
`git checkout .`
# 需求三：将 stage 区的文件添加到 history 区——`git commit`
`git commit -m '一些描述'`
再简单提一些常见场景， 比如说 commit 完之后，突然发现一些错别字需要修改，又不想为改几个错别字而新开一个 commit 到 history 区，那么就可以使用下面这个命令：
`git commit --amend`

# 需求四：将 history 区的文件还原到 stage 区——`git reset`（用commit还原stage）
这个需求很常见，比如说我用了一个 git add . 一股脑把所有修改加入 stage，但是突然想起来文件 a.txt 中的代码我还没写完，不应该把它 commit 到 history 区，所以我得把它从 stage 中撤销，等后面我写完了再提交。
例如：
`bash
git status
On branch master
Changes to be committed:
	modified:   a.txt
	modified:   b.txt`
如何把 a.txt 从 stage 区还原出来呢？可以使用 git reset 命令： 
`bash 
$ git reset a.txt
$ git status
On branch master
Changes to be committed:
	modified:   b.txt

Changes not staged for commit:
	modified:   a.txt`

上面的这个命令是一个简写，实际上 reset 命令的完整写法如下：
`git reset --mixed HEAD a.txt`
**该命令的自然语言描述是：不改变 work dir 中的任何数据，将 stage 区域中的 a.txt 文件还原成 HEAD 指向的 commit history 中的样子。**

# 需求五：将 work dir 的修改提交到 history 区——`git commit -a`
这个需求很简单，先 git add 然后 git commit 就行了，或者一个快捷方法是使用命令 git commit -a。

# 需求六：将 history 区的历史提交还原到 work dir 中`git checkout HEAD .`
`bash
$ git checkout HEAD .
Updated 12 paths from d480c4f
`
这样，work dir 和 stage 中所有的「修改」都会被撤销，恢复成 HEAD 指向的那个 history commit。
只要找到任意一个 commit 的 HASH 值，checkout 命令可就以将文件恢复成任一个 history commit 中的样子
`bash 
git checkout 2bdf04a some_test.go
Updated 1 path from 2bdf04a`
使用建议：谨慎使用。
理由：这个操作会将指定文件在 work dir 的数据恢复成指定 commit 的样子，且会删除该文件在 stage 中的数据，都无法恢复，所以应该慎重使用。

# 一些技巧
## 1. 合并多个 commit
`bash
git reset 17bd20c
git add .
git commit -m 'balabala'
`
reset之后HEAD指向17bd20c这个commit，然后再合并
## 2. 由于 HEAD 指针的回退，导致有的 commit 在 git log 命令中无法看到，怎么得到它们的 Hash 值呢？
看不到某些 commit 只是因为它们不是我们当前 HEAD 位置的「历史」提交，我们可以使用如下命令查看操作记录：
`bash
$ git reflog
`
## 3. 怎么解决冲突？
使用可视化Git工具