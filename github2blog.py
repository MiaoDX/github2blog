#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The code of gitbub2blog
"""

def get_gitbub_folder(git_user_name, project_name , branch_name='master', folder_or_file_name='', target_folder='tmp'):
    """
    Ref [Download a single folder or directory from a GitHub repo](https://stackoverflow.com/a/18324458/7067150)
    """
    import subprocess

    git_url = 'https://github.com/' + git_user_name + '/' + project_name + '.git/branches/' + branch_name + '/' + folder_or_file_name

    # we should check it
    # ls_cmd = 'svn ls ' + git_url
    # ls_ans = subprocess.run(ls_cmd)
    
    target_folder += '/' # avoid the potential possibility of forgetting /
    if folder_or_file_name[-2:] == 'md': # file name, like README.md
        target_folder += folder_or_file_name.split('.')[0]
    else:
        target_folder += folder_or_file_name

    print("target folder:{}".format(target_folder))
    input()

    export_cmd = "svn export " + git_url + ' ' + target_folder + ' --force'
    print(export_cmd)

    subprocess.run(export_cmd)
    # contents 

def post_process():
    pass

if __name__ == '__main__':
    git_user_name = 'MiaoDX'
    project_name = 'opencv_scripts'
    branch_name='master'
    folder='opencv_gpu'
    file = "README.md"


    blog_local = r'H:\blog_and_translation_and_other_gits\hexo_dir\source\_posts\blogs'

    get_gitbub_folder(git_user_name, project_name, folder_or_file_name=folder, target_folder=blog_local)
    # get_gitbub_folder(git_user_name, project_name, folder_or_file_name=file, target_folder=blog_local)