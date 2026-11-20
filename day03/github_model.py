from pydantic import BaseModel,ValidationError,Field
import httpx
class GitHubUser(BaseModel):
    login: str
    public_repos: int
    followers: int
    bio: str | None = None

response=httpx.get("https://api.github.com/users/mohammed-noushad-rafi",timeout=10)
user = GitHubUser.model_validate(response.json())
print(user.login,user.public_repos,user.bio)
try:
     data=GitHubUser.model_validate({"login": "https://api.github.com/users/mohammed-noushad-rafi",
                            "public_repos": "4"})
     data.aise_for_status()
except ValidationError as e:
     print(f"report {e}")