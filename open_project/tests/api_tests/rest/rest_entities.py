class OpenProjectEntities:

    @staticmethod
    def get_project_create_body(project_name: str, description: str = 'default project description') -> dict:
        return {
            "name": project_name,
            "description": {
                "raw": description
            }
        }

    @staticmethod
    def get_project_update_body(description) -> dict:
        return {
            "description": {
                "raw": description
            }
        }

    @staticmethod
    def get_create_work_package_body(pkg_name: str, project_ref: str, pkg_type: str) -> dict:
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

    @staticmethod
    def get_work_package_update_body(lock_version: int, description: str = "default package description") -> dict:
        return {
            "lockVersion": lock_version,
            "_links": {},
            "description": {
                "raw": description
            }
        }
