#!/usr/bin/env python
import github

import math
import os

user = os.getenv('GH_USER')
gh = github.GitHub()

# number of results per page, github default is 30:
R_PAGE = 30


def getuser(gh, user):
    """return basic user information"""
    return gh.users(user).get()


def getuserrepos(gh, user):
    """return a user's repos"""
    repos = list()
    pages = int(math.ceil(n_public_repos(gh, user) / float(R_PAGE)))
    for i in range(pages):
        # github index their pages from 1, hence the +1
        qs = user + "/repos?page=" + str(i + 1)
        repos.extend(gh.users(qs).get())
    return repos


def getuserrepos_keys(gh, user):
    """return just key fields, for examination"""
    repos = getuserrepos(gh, user)
    return repos[0].keys()


def urls(gh, user):
    """list of urls of a user's repos"""
    return [repo.url for repo in getuserrepos(gh, user)]


def reponames(gh, user):
    """return list of repository names for a user"""
    return [u.split('/')[-1] for u in urls(gh, user)]


def n_public_repos(gh, user):
    """number of public repositories of a user"""
    return getuser(gh, user).public_repos


def main():
    gh = github.GitHub()
    user = os.getenv('GH_USER')
    # print (getuser(gh, user))
    # print (getuserrepos(gh, user))
    # for i in getuserrepos_keys(gh, user):
    #    print (i)
    #    continue
    # print n_public_repos(gh, user)
    # print('\n\n\n')
    for i in reponames(gh, user):
        print (i)


if __name__ == "__main__":
    main()
