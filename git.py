import git
remoteurl="https://github.com/saisarankanisetty/demo.git"
localfolder="E:\demo"
myrepo = git.Repo.clone_from(remoteurl, localfolder)
myrepo.git.checkout("main")