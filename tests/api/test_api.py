import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == 'Ola'


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Kliuch'

@pytest.mark.api
def test_emojis_exist(github_api):
    emojis = github_api.get_emojis()
    assert 'smile' in emojis
    assert emojis['smile'].startswith('https://')

@pytest.mark.api
def test_commits_return_list(github_api):
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert isinstance(commits, list)
    assert 'commit' in commits[0]

@pytest.mark.api
def test_commit_has_author(github_api):
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert commits[0]['commit']['author']['name'] is not None

@pytest.mark.api
def test_commit_message_contains_text(github_api):
    commits = github_api.get_commits('octocat', 'Hello-World')
    message = commits[0]['commit']['message']
    assert isinstance(message, str)
    assert len(message) > 0