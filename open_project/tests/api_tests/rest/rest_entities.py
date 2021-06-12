class OpenProjectEntities:

    def get_project_create_body(self, project_name: str, description: str = 'default project description') -> dict:
        return {
            "name": project_name,
            "description": {
                "raw": description
            }
        }

    def get_project_update_body(self, description) -> dict:
        return {
            "description": {
                "raw": description
            }
        }

    def get_create_work_package_body(self, pkg_name: str, project_ref: str, pkg_type: str) -> dict:
        return {
            "subject": pkg_name,
            "percentageDone": 0,
            "_links": {
                "type": {
                    "href": pkg_type
                },
                "project": {
                    "href": project_ref
                }
            }
        }

    def get_work_package_update_body(self, lock_version: int, description: str = "default package description") -> dict:
        return {
            "lockVersion": lock_version,
            "_links": {},
            "description": {
                "raw": description
            }
        }
