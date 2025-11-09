create or replace database sales;
create schema sales.hr;
use schema sales.hr;
show secrets;
show api integrations;
show git repositories;

create or replace secret my_github_scret
type=password
username='jitechau01'
password='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'; --this value is retrived from github classic token

--create github api integration object
create or replace api integration my_git_api_integration
api_provider=git_https_api
api_allowed_prefixes=('https://github.com/jitechau01/')
allowed_authentication_secrets=(my_github_scret)
enabled=true;

--create git reposiory parallel to 
create or replace git repository my_github_repo
api_integration=my_git_api_integration
git_credentials=my_github_scret
origin='https://github.com/jitechau01/codeplace';

--check branches in the repository
show git branches in git repository MY_GITHUB_REPO;

