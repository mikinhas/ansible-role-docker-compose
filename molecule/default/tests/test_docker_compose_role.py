def test_if_python3_pip_package_is_installed(host):
    package = host.package("python3-pip")
    assert package.is_installed


def test_if_docker_pip_package_is_installed(host):
    package = host.pip("docker")
    assert package.is_installed


def test_if_docker_service_is_up(host):
    service = host.service("docker")
    assert service.is_enabled
    assert service.is_running


def test_if_docker_compose_pip_package_is_installed(host):
    package = host.pip("docker-compose")
    assert package.is_installed


def test_if_docker_compose_project_directory_exists(host):
    directory_path = host.file("/home/vagrant/molecule/nginx")
    assert directory_path.is_directory


def test_if_docker_compose_file_exists(host):
    directory_path = host.file("/home/vagrant/molecule/nginx/docker-compose.yml")
    assert directory_path.is_file
