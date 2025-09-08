import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api 
def test_user_exists(github_api):
    r = github_api.get_user('kliucholga')
    assert r['message'] == 'Not Found'


@pytest.mark.api            # тест на пошук репозиторію який існує
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('automation_tests_modul12.3')
    assert r['total_count'] == 1
    assert 'automation_tests_modul12.3' in r['items'][0]['name']

@pytest.mark.api    # тест на пошук репозиторію якого не існує
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('automation_tests_modul12.3_non')
    assert r['total_count'] == 0


@pytest.mark.api # тест на пошук репозиторію з 1 символом
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
        