import os
import pytest
from ethereum.tools import testutils

fixtures = testutils.get_tests_from_file_or_dir(
    os.path.join(testutils.fixture_path, 'PoWTests'))


@pytest.mark.xfail
def test_pow():
    raise Exception('not implemented error')
