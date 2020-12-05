import itertools
from pathlib import Path

from setuptools import setup, Command, find_packages

BASE_DIR = Path('.')


class NoOptionsCommand(Command):
    """ 无配置命令 """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class D2U(NoOptionsCommand):
    description = R"文档换行符转换，\r\n to \r."

    @classmethod
    def dos2unix(cls, infile, outfile):
        with open(infile, 'rb') as f:
            content = f.read()
        with open(outfile, 'wb') as f:
            for line in content.splitlines():
                f.write(line + b'\n')

    def run(self):
        """ 搜索并转换为unix换行符 """
        extends = ['*.yaml', '*.md', '*.sh']
        for pth in itertools.chain(*(BASE_DIR.rglob(ext) for ext in extends)):
            self.dos2unix(pth, pth)


class GenerateConfig(NoOptionsCommand):
    description = "生成配置."

    def run(self):
        # 生成配置
        pth = Path() / 'instance'
        pth.mkdir(exist_ok=True)


setup(
    name='template_server',
    version='1.0',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    package_data={'': ['*.txt']},
    include_package_data=True,
    cmdclass={
        'd2u': D2U,
        'gen_cfg': GenerateConfig
    },
    install_requires=[
        "passlib",
        "flask-cors",
        "flask",
        "flask-migrate",
        "python-dotenv"
    ]
)
