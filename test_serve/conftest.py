def pytest_addoption(parser):
    parser.addoption(
        "--address",
        action="store",
        default="127.0.0.1",
        help="ip address of the torchserve server",
    )
    parser.addoption(
        "--modelName",
        action="store",
        default="cifar",
        help="name of the hosted model",
    )


def pytest_generate_tests(metafunc):
    if "address" in metafunc.fixturenames:
        metafunc.parametrize("address", [metafunc.config.getoption("address")])
    if "modelName" in metafunc.fixturenames:
        metafunc.parametrize("modelName", [metafunc.config.getoption("modelName")])
