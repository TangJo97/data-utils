import requests as r
import json
import argparse


my_parser = argparse.ArgumentParser(
    description="Upload to a comment to Github"
)
my_parser.add_argument(
    "repo_name",
    metavar="repo_name",
    type=str,
    help="name of the owner & repo, e.g. TangJo97/data-utils",
)

my_parser.add_argument(
    "issue_number",
    metavar="issue_number",
    type=int,
    help="The issue number of the PR",
)

my_parser.add_argument(
    "file_to_post",
    metavar="file_to_post",
    type=str,
    help="The file to be read & posted",
)

my_parser.add_argument(
    "token",
    metavar="token",
    type=str,
    help="The auth token",
)
args = my_parser.parse_args()
with open(args.file_to_post) as f:
    comment = f.read()
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {args.token}"
}
response = r.post(f"https://api.github.com/repos/{args.repo_name}/issues/{args.issue_number}/comments", 
data = json.dumps({"body": comment}),
headers = headers)

print(response)