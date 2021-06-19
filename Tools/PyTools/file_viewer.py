import glob
import os


def filepath_list(target_dir):
    target_dir_path_list = glob.glob(current_dir_path + "/*")
    return get_filepath_as_a_list(target_dir_path_list)


def get_filepath_as_a_list(file_path_list):

    if not file_path_list:
        return []

    result, next_path_list = get_next_path_list(file_path_list)
    path_list = []
    for path in next_path_list:
        path_list += glob.glob(path + "/*")
    return result + get_filepath_as_a_list(path_list)


def get_next_path_list(file_path_list):

    result, next_path_list = [], []
    for path in file_path_list:
        if os.path.isfile(path):
            result.append(path)

        if os.path.isdir(path) and not glob.glob(path + "/*"):
            result.append(path)

        next_path_list.append(path)

    return result, next_path_list
    

if __name__ == '__main__':

    target_dir_path = os.getcwd()
    file_path_list = filepath_list(target_dir_path)

    for path in file_path_list:
        print(path)

