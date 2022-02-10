import pytest

from default.test_rdm import test_rdm
from default.test_rdm import test_rdm_bw_functional
from default.test_rdm import test_rdm_atomic


@pytest.fixture(scope="module", params=["host_to_host", "host_to_cuda",
                                        "cuda_to_host", "cuda_to_cuda"])
def memory_type(request):
    return request.param

def run_rdm_test(cmdline_args, executable, iteration_type, completion_type, memory_type, message_size):
    from common import ClientServerTest
    test = ClientServerTest(cmdline_args, executable, iteration_type,
                            completion_type=completion_type,
                            datacheck_type="with_datacheck",
                            message_size=message_size,
                            memory_type=memory_type)
    test.run()

@pytest.mark.parametrize("iteration_type",
                         [pytest.param("short", marks=pytest.mark.short),
                          pytest.param("standard", marks=pytest.mark.standard)])
def test_rdm_pingpong(cmdline_args, iteration_type, completion_type, memory_type):
    run_rdm_test(cmdline_args, "fi_rdm_pingpong", iteration_type,
            completion_type, memory_type, "all")

@pytest.mark.parametrize("message_size",
                         [pytest.param("r:8000,4,9000", marks=pytest.mark.short)])
def test_rdm_pingpong_range(cmdline_args, completion_type, memory_type, message_size):
    run_rdm_test(cmdline_args, "fi_rdm_pingpong", "short",
                 completion_type, memory_type, message_size)

@pytest.mark.parametrize("iteration_type",
                         [pytest.param("short", marks=pytest.mark.short),
                          pytest.param("standard", marks=pytest.mark.standard)])
def test_rdm_tagged_pingpong(cmdline_args, iteration_type, completion_type, memory_type):
    run_rdm_test(cmdline_args, "fi_rdm_tagged_pingpong", iteration_type,
                 completion_type, memory_type, "all")

@pytest.mark.parametrize("message_size",
                         [pytest.param("r:8000,4,9000", marks=pytest.mark.short)])
def test_rdm_tagged_pingpong_range(cmdline_args, completion_type, memory_type, message_size):
    run_rdm_test(cmdline_args, "fi_rdm_tagged_pingpong", "short",
                 completion_type, memory_type, message_size)

@pytest.mark.parametrize("iteration_type",
                         [pytest.param("short", marks=pytest.mark.short),
                          pytest.param("standard", marks=pytest.mark.standard)])
def test_rdm_tagged_bw(cmdline_args, iteration_type, completion_type, memory_type):
    run_rdm_test(cmdline_args, "fi_rdm_tagged_bw", iteration_type,
                 completion_type, memory_type, "all")

@pytest.mark.parametrize("message_size",
                         [pytest.param("r:8000,4,9000", marks=pytest.mark.short)])
def test_rdm_tagged_bw_range(cmdline_args, completion_type, memory_type, message_size):
    run_rdm_test(cmdline_args, "fi_rdm_tagged_bw", "short",
                 completion_type, memory_type, message_size)
