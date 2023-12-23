import httpx
import json

USERNAME = "admin"


class WindmillClient:
    _url: str
    _token: str
    _workspace: str

    _client: httpx.Client

    def __init__(self):
        self._workspace = "integration-tests"
        self._url = "http://localhost:8000"
        self._token = self._login()

        self._client = self._init_client()
        self._create_workspace()

    def __del__(self):
        self._logout()
        self._client.close()

    def _login(self) -> str:
        with httpx.Client(base_url=self._url) as unauth_client:
            response = unauth_client.post(
                "/api/auth/login",
                json={
                    "email": "admin@windmill.dev",
                    "password": "changeme",
                },
            )
            if response.status_code // 100 != 2:
                raise Exception(response.content.decode())
            return response.content.decode()

    def _logout(self) -> None:
        response = self._client.post(
            "/api/auth/logout",
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())

    def _init_client(self):
        token = self._token
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        return httpx.Client(
            base_url=self._url,
            headers=headers,
        )

    def _create_workspace(self):
        exists = self._client.post(
            "/api/workspaces/exists",
            json={
                "id": self._workspace,
            },
        )
        if exists.status_code // 100 == 2 and exists.content.decode() == "true":
            print("Workspace already exists, not creating it")
            return
        response = self._client.post(
            "/api/workspaces/create",
            json={
                "id": self._workspace,
                "name": self._workspace,
                "username": "admin",
            },
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.content.decode()

    def run_sync(self, path: str, args: dict, type: str = "p"):
        response = self._client.post(
            f"/api/w/{self._workspace}/jobs/run_wait_result/{type}/{path}",
            json=args,
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.json()

    def create_script(self, path: str, content: str, language: str):
        response = self._client.post(
            f"/api/w/{self._workspace}/scripts/create",
            json={
                "path": path,
                "content": content,
                "description": "",
                "summary": "",
                "language": language,
            },
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.content.decode()

    def delete_script(self, path: str):
        response = self._client.post(
            f"/api/w/{self._workspace}/scripts/delete/p/{path}",
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.content.decode()

    def create_flow(self, path: str, flow_value_json: str):
        parsed_flow = json.loads(flow_value_json)
        if "path" not in parsed_flow:
            parsed_flow["path"] = path
        response = self._client.post(
            f"/api/w/{self._workspace}/flows/create",
            json=parsed_flow,
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.content.decode()

    def delete_flow(self, path: str):
        response = self._client.delete(
            f"/api/w/{self._workspace}/flows/delete/{path}",
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.content.decode()

    def create_schedule(
        self,
        path: str,
        runnable_path: str,
        type: str = "script",
        schedule: str = "*/5 * * * * *",
        args: dict = {},
    ):
        response = self._client.post(
            f"/api/w/{self._workspace}/schedules/create",
            json={
                "path": path,
                "schedule": schedule,
                "timezone": "Europe/Paris",
                "script_path": runnable_path,
                "is_flow": type == "flow",
                "args": args,
                "enabled": True,
            },
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.content.decode()

    def delete_schedule(self, path: str):
        response = self._client.delete(
            f"/api/w/{self._workspace}/schedules/delete/{path}",
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.content.decode()

    def get_latest_job_runs(self, path: str):
        response = self._client.get(
            f"/api/w/{self._workspace}/jobs/list?script_path_exact={path}"
        )
        if response.status_code // 100 != 2:
            raise Exception(response.content.decode())
        return response.json()

    def get_version(self):
        response = self._client.get("/api/version")
        return response.content.decode()


if __name__ == "__main__":
    client = WindmillClient()
    client.create_script(
        "u/admin/test_script", "def main(x: int):\n    return x", "python3"
    )
    print(client.get_version())
