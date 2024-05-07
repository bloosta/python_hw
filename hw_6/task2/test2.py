import pytest
from func2 import merge_and_write

@pytest.fixture
def testing_files(tmp_path):
    file1 = tmp_path / 'file1.txt'
    file2 = tmp_path / 'file2.txt'
    with open(file1, 'w') as f1:
        f1.write('task2')
    with open(file2, 'w') as f2:
        f2.write('hw6')
    output_file = tmp_path / 'output.txt'

    return file1, file2, output_file

def testing_output(testing_files):
    file1, file2, output_file = testing_files
    assert merge_and_write(file1, file2, output_file) == 'task2 hw6'

def testing_exist(testing_files):
    file1, file2, output_file = testing_files
    assert merge_and_write(file1, 'test_file.txt', output_file) == "Один из файлов не найден"
    assert merge_and_write('test_file.txt', file2, output_file) == "Один из файлов не найден"
    assert merge_and_write('test_file1.txt', 'test_file2.txt', output_file) == "Один из файлов не найден"
