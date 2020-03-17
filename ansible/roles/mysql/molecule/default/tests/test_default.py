import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mysql_port(host):
    mysql = host.addr("127.0.0.1")
    mysql.port(3306).is_reachable


def test_mysql_file(host):
    os = host.system_info.distribution
    if os == 'debian':
        f = host.file('/etc/mysql/my.cnf')
        assert f.exists
        assert f.is_file
        assert f.user == 'root'
        assert f.group == 'root'
        assert f.mode == 0o644
    elif os == 'ubuntu':
        f = host.file('/etc/mysql/my.cnf')
        assert f.exists
        assert f.is_file
        assert f.user == 'root'
        assert f.group == 'root'
        assert f.mode == 0o644
    elif os == 'centos':
        f = host.file('/etc/my.cnf')
        assert f.exists
        assert f.is_file
        assert f.user == 'root'
        assert f.group == 'root'
        assert f.mode == 0o644


def test_chrony_is_running(host):
    if os == 'debian':
        service = host.service('mysql')
        assert service.is_running
    elif os == 'ubuntu':
        service = host.service('mysql')
        assert service.is_running
    elif os == 'centos':
        service = host.service('mariadb')
        assert service.is_running
