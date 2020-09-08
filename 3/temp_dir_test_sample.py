import json
import os

from sample import save_dict

''' You can use the tmp_path fixture which will provide a temporary directory unique to the test invocation, created in the base temporary directory.'''


def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "saved\n"
