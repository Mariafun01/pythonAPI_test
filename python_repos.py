"""
程序自动执行API调用并处理结果，
以找出GitHub上星级最高的Python项目
"""
import requests

# 执行API调用并存储响应。
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers)
print(f"Status code:{r.status_code}")
# 将API响应赋给一个变量。
response_dict=r.json()

# 处理结果
print(f"Total repositories: {response_dict['total_count']}")

# 探索有关仓库的信息
repo_dicts=response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    # print(f"Created: {repo_dict['created_at']}")
    # print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")