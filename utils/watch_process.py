import os
from pyserverchan import pyserver
import time


def watch_python():
    result = "function watch_python():"
    try:
        python_pid = os.popen('pidof python').read().split()
        if len(python_pid) == 1:
            return "No python found!!!"
        result += os.popen(f'top -p {",".join(python_pid)} -c -b -n1').read()
    except BaseException:
        result += "watch_python() failed"
    return result

def watch_folder(file_path):
    result = f"function watch_folder({file_path}):"
    try:
        result += os.popen(f'ls -alh {file_path}').read()
    except BaseException:
        result += f"watch_folder({file_path}) failed"
    return result

def single_watch():
    now_time = time.asctime(time.localtime(time.time()))
    result_python = watch_python()
    result_folder1 = watch_folder("~/user001/thuys/specter_fast/model/")
    result_word2vec = watch_folder("~/user001/thuys/embedding/word2vec/")
    result_glove = watch_folder("~/user001/thuys/embedding/glove/")
    result = os.linesep.join([now_time, result_python, result_folder1, result_word2vec, result_glove])
    result = result.replace(os.linesep, os.linesep + os.linesep)
    
    if result_python == "No python found!!!":
        result = result_python

    #print(result)
    svc = pyserver.ServerChan()
    svc.output_to_weixin(title='Jiangsu_GPU Server Python Process', content=result)
    
    if result == "No python found!!!":
        return 1
    return 0

def main():
    no_python_count = 0
    no_python_count += single_watch()
    while no_python_count < 3:
        time.sleep(3600 * 3)
        no_python_count += single_watch()

if __name__ == "__main__":
    main()

