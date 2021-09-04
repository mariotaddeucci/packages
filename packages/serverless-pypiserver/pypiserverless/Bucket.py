from os import path

import boto3

from .core import guess_pkgname_and_version


class Bucket:

    _s3 = None

    @staticmethod
    def setup(bucket, packages_dir="/", client={}):
        Bucket._bucket = bucket
        Bucket._packages_dir = packages_dir.rstrip("/") + "/"
        Bucket._s3 = boto3.client("s3", **client)

    @staticmethod
    def get_file_url(filename):

        url = Bucket._s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": Bucket._bucket,
                "Key": path.join(Bucket._packages_dir, filename),
            },
            ExpiresIn=300,
        )

        return url

    @staticmethod
    def packages(pkg_name=None):

        prefix = pkg_name or ""
        prefix = Bucket._packages_dir + prefix

        all_files = Bucket._s3.list_objects(
            Bucket=Bucket._bucket, Prefix=prefix, Delimiter="/"
        ).get("Contents", [])

        for f in all_files:

            pkg = {}
            pkg["uri"] = f["Key"]
            pkg["filename"] = path.basename(pkg["uri"])

            res = guess_pkgname_and_version(pkg["uri"])

            if res is None:
                continue

            pkg["name"], pkg["version"] = res
            if not pkg_name is None and pkg_name != pkg["name"]:
                continue

            return pkg
