import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgres_is_installed(host):
    oracle_java8 = host.package("postgresql-9.6")
    assert oracle_java8.is_installed
