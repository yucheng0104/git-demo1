# GIT-DEMO

### 檢視版本
- git --version

### 建立全域端使用者
- git config --global user.name xx
- git config --global user.email xxx@gmail.com

### 檢視 git 設定
- git config --list 

### vscode
- command+shift+p
  - 選擇 default
    - terminal zsh

<hr>

### 控管專案
- git init

### 檔案加入控管
- git add . (全部新增)
- git add filename (指定新增文件)
    - Untrack => Added => Modifile => Deleted

### 檢視控管狀態
- git status

### 檢視暫存區目前控管的內容
  - git ls-files -s

### 檢視物件內容（t:型態,ｐ:內容）
- git cat-file -t shal(2+4)
- git cat-file -p shal(2+4)
  - 檢視內容 

### Added => Modifile
  - git status
  - git add filename(確認修改)

### 反悔修改
  - git restore filename


### 記錄到倉庫區 
- git commit -m "message"
- git commit -am "message"
  - a => add
  
#### 開啟 vim 編輯器
- git commit
  - i 切換 insert 模式
  - esc 切換功能
    - :wq(寫入離開)
    - :q! 不存存離開 
#### 合併上一次 commit
-  git add .
-  git commit --amend

### 檢視目前 commit
- git log
- git log --oneline
  
### 指令刪除
- git rm -f filename (強制刪除)
  - git restore --staged filename (恢復)

### 將檔案移出 (暫存/倉庫) 
- git rm --cached filename


<hr>

### 檢視分支
- git branch 
  - 預設為 master  (需有 commit 才會出現)

### 新增分支
- git branch 分支名稱

### 切換分支

- git checkout 分支名稱

### 新增＋切換分支
- git checkout -b 分支名稱

### 合併分支
- git checkout master
  - git merge 分支名稱

### 刪除分支
- git branch -D 分支名稱

### 合併衝突
- 不同分支改動同一個檔案(選擇合併方式)
- git merge --abort(反悔合併)

### 切換commit
- git checkout commit-shal
  - 回到過去的修正
    - 新增分支跟commit
    - 切回 master進行合併 
  - 回到最新位置
    - git checkout master

### 重置指令
- git reset commit-shal
- git reset --hard commit-shal
- git reset ORIG_HEAD (恢復動作)
- git reset --hard HEAD(重置到最新commit)
- git reset --hard HEAD~n(重置到最新commit的前n個)

### 檢視所有歷程
- git reflog
  - 可以觀察 commit-shal ,進行 reset(重置指令)

### git hub
- echo "# git-demo1" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/yucheng0104/git-demo1.git
- git push -u origin main

### 綁定github雲端的倉庫
- git remote add origin https://github.com/yucheng0104/git-demo1.git
- git remote -v
  - 檢視綁定倉庫的URL
  
### 本地同步雲端
- git push
  - git push --set-upstream origin master
  - git push -u origin master

### 複製專案
- git clone https://github.com/yucheng0104/git-demo1.git