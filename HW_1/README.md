Домашняя работа к занятию “Docker и микросервисная архитектура”

[Докер-файл](Dockerfile)

Лог сборки:

```shell
Deploying 'netology-ml:netology-ml Dockerfile: netology-ds/HW_1/Dockerfile'...
Building image...
Preparing build context archive...
[==================================================>]3/3 files
Done

Sending build context to Docker daemon...
[==================================================>] 3.254kB
Done

Step 1/6 : FROM continuumio/miniconda3:latest
 ---> 67414e5844b6
Step 2/6 : LABEL mainteiner="Vladimir Leshnevskij"
 ---> Running in a04e44c365c0
Removing intermediate container a04e44c365c0
 ---> 15350dd1fdf3
Step 3/6 : RUN set -x     && apt-get update -yqq     && apt-get upgrade -yqq     && python3 -m venv /env     && . /env/bin/activate     && pip install -U pip     && pip install mlflow boto3 pymysql     && apt-get purge -yqq     && apt-get autoremove -yqq     && apt-get clean     && rm -rf         /var/lib/apt/lists/*         /tmp/*         /var/tmp/*         /usr/share/man         /usr/share/doc         /usr/share/doc-base
 ---> Running in 4fd4341b8164
+ apt-get update -yqq
+ apt-get upgrade -yqq
debconf: delaying package configuration, since apt-utils is not installed
(Reading database ... 12133 files and directories currently installed.)
Preparing to unpack .../libgssapi-krb5-2_1.17-3+deb10u2_amd64.deb ...
Unpacking libgssapi-krb5-2:amd64 (1.17-3+deb10u2) over (1.17-3+deb10u1) ...
Preparing to unpack .../libkrb5-3_1.17-3+deb10u2_amd64.deb ...
Unpacking libkrb5-3:amd64 (1.17-3+deb10u2) over (1.17-3+deb10u1) ...
Preparing to unpack .../libkrb5support0_1.17-3+deb10u2_amd64.deb ...
Unpacking libkrb5support0:amd64 (1.17-3+deb10u2) over (1.17-3+deb10u1) ...
Preparing to unpack .../libk5crypto3_1.17-3+deb10u2_amd64.deb ...
Unpacking libk5crypto3:amd64 (1.17-3+deb10u2) over (1.17-3+deb10u1) ...
Setting up libkrb5support0:amd64 (1.17-3+deb10u2) ...
Setting up libk5crypto3:amd64 (1.17-3+deb10u2) ...
Setting up libkrb5-3:amd64 (1.17-3+deb10u2) ...
Setting up libgssapi-krb5-2:amd64 (1.17-3+deb10u2) ...
Processing triggers for libc-bin (2.28-10) ...
+ python3 -m venv /env
+ . /env/bin/activate
+ deactivate nondestructive
+ [ -n  ]
+ [ -n  ]
+ [ -n  -o -n  ]
+ [ -n  ]
+ unset VIRTUAL_ENV
+ [ ! nondestructive = nondestructive ]
+ VIRTUAL_ENV=/env
+ export VIRTUAL_ENV
+ _OLD_VIRTUAL_PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
+ PATH=/env/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
+ export PATH
+ [ -n  ]
+ [ -z  ]
+ _OLD_VIRTUAL_PS1=# 
+ PS1=(env) # 
+ export PS1
+ [ -n  -o -n  ]
+ pip install -U pip
Requirement already satisfied: pip in /env/lib/python3.9/site-packages (21.1.1)
Collecting pip
  Downloading pip-21.2.3-py3-none-any.whl (1.6 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.1.1
    Uninstalling pip-21.1.1:
      Successfully uninstalled pip-21.1.1
Successfully installed pip-21.2.3
+ pip install mlflow boto3 pymysql
Collecting mlflow
  Downloading mlflow-1.19.0-py3-none-any.whl (14.4 MB)
Collecting boto3
  Downloading boto3-1.18.16-py3-none-any.whl (131 kB)
Collecting pymysql
  Downloading PyMySQL-1.0.2-py3-none-any.whl (43 kB)
Collecting gunicorn
  Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
Collecting gitpython>=2.1.0
  Downloading GitPython-3.1.18-py3-none-any.whl (170 kB)
Collecting pyyaml>=5.1
  Downloading PyYAML-5.4.1-cp39-cp39-manylinux1_x86_64.whl (630 kB)
Collecting entrypoints
  Downloading entrypoints-0.3-py2.py3-none-any.whl (11 kB)
Collecting requests>=2.17.3
  Downloading requests-2.26.0-py2.py3-none-any.whl (62 kB)
Collecting prometheus-flask-exporter
  Downloading prometheus_flask_exporter-0.18.2.tar.gz (22 kB)
Collecting sqlparse>=0.3.1
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting pytz
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting Flask
  Downloading Flask-2.0.1-py3-none-any.whl (94 kB)
Collecting docker>=4.0.0
  Downloading docker-5.0.0-py2.py3-none-any.whl (146 kB)
Collecting querystring-parser
  Downloading querystring_parser-1.2.4-py2.py3-none-any.whl (7.9 kB)
Collecting packaging
  Downloading packaging-21.0-py3-none-any.whl (40 kB)
Collecting click>=7.0
  Downloading click-8.0.1-py3-none-any.whl (97 kB)
Collecting numpy
  Downloading numpy-1.21.1-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (15.8 MB)
Collecting cloudpickle
  Downloading cloudpickle-1.6.0-py3-none-any.whl (23 kB)
Collecting alembic<=1.4.1
  Downloading alembic-1.4.1.tar.gz (1.1 MB)
Collecting sqlalchemy
  Downloading SQLAlchemy-1.4.22-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
Collecting protobuf>=3.7.0
  Downloading protobuf-3.17.3-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.0 MB)
Collecting pandas
  Downloading pandas-1.3.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
Collecting databricks-cli>=0.8.7
  Downloading databricks-cli-0.15.0.tar.gz (56 kB)
Collecting jmespath<1.0.0,>=0.7.1
  Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
Collecting botocore<1.22.0,>=1.21.16
  Downloading botocore-1.21.16-py3-none-any.whl (7.8 MB)
Collecting s3transfer<0.6.0,>=0.5.0
  Downloading s3transfer-0.5.0-py3-none-any.whl (79 kB)
Collecting Mako
  Downloading Mako-1.1.4-py2.py3-none-any.whl (75 kB)
Collecting python-editor>=0.3
  Downloading python_editor-1.0.4-py3-none-any.whl (4.9 kB)
Collecting python-dateutil
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting urllib3<1.27,>=1.25.4
  Downloading urllib3-1.26.6-py2.py3-none-any.whl (138 kB)
Collecting tabulate>=0.7.7
  Downloading tabulate-0.8.9-py3-none-any.whl (25 kB)
Collecting six>=1.10.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting websocket-client>=0.32.0
  Downloading websocket_client-1.1.1-py2.py3-none-any.whl (68 kB)
Collecting gitdb<5,>=4.0.1
  Downloading gitdb-4.0.7-py3-none-any.whl (63 kB)
Collecting smmap<5,>=3.0.1
  Downloading smmap-4.0.0-py2.py3-none-any.whl (24 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.2-py3-none-any.whl (59 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2021.5.30-py2.py3-none-any.whl (145 kB)
Collecting charset-normalizer~=2.0.0
  Downloading charset_normalizer-2.0.4-py3-none-any.whl (36 kB)
Collecting greenlet!=0.4.17
  Downloading greenlet-1.1.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (147 kB)
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.0.1-py3-none-any.whl (288 kB)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.0.1-py3-none-any.whl (133 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.0.1-cp39-cp39-manylinux2010_x86_64.whl (30 kB)
Requirement already satisfied: setuptools>=3.0 in /env/lib/python3.9/site-packages (from gunicorn->mlflow) (56.0.0)
Collecting pyparsing>=2.0.2
  Downloading pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
Collecting prometheus_client
  Downloading prometheus_client-0.11.0-py2.py3-none-any.whl (56 kB)
Using legacy 'setup.py install' for alembic, since package 'wheel' is not installed.
Using legacy 'setup.py install' for databricks-cli, since package 'wheel' is not installed.
Using legacy 'setup.py install' for prometheus-flask-exporter, since package 'wheel' is not installed.
Installing collected packages: six, MarkupSafe, Werkzeug, urllib3, smmap, python-dateutil, jmespath, Jinja2, itsdangerous, idna, greenlet, click, charset-normalizer, certifi, websocket-client, tabulate, sqlalchemy, requests, pytz, python-editor, pyparsing, prometheus-client, numpy, Mako, gitdb, Flask, botocore, sqlparse, s3transfer, querystring-parser, pyyaml, protobuf, prometheus-flask-exporter, pandas, packaging, gunicorn, gitpython, entrypoints, docker, databricks-cli, cloudpickle, alembic, pymysql, mlflow, boto3
    Running setup.py install for prometheus-flask-exporter: started
    Running setup.py install for prometheus-flask-exporter: finished with status 'done'
    Running setup.py install for databricks-cli: started
    Running setup.py install for databricks-cli: finished with status 'done'
    Running setup.py install for alembic: started
    Running setup.py install for alembic: finished with status 'done'
Successfully installed Flask-2.0.1 Jinja2-3.0.1 Mako-1.1.4 MarkupSafe-2.0.1 Werkzeug-2.0.1 alembic-1.4.1 boto3-1.18.16 botocore-1.21.16 certifi-2021.5.30 charset-normalizer-2.0.4 click-8.0.1 cloudpickle-1.6.0 databricks-cli-0.15.0 docker-5.0.0 entrypoints-0.3 gitdb-4.0.7 gitpython-3.1.18 greenlet-1.1.1 gunicorn-20.1.0 idna-3.2 itsdangerous-2.0.1 jmespath-0.10.0 mlflow-1.19.0 numpy-1.21.1 packaging-21.0 pandas-1.3.1 prometheus-client-0.11.0 prometheus-flask-exporter-0.18.2 protobuf-3.17.3 pymysql-1.0.2 pyparsing-2.4.7 python-dateutil-2.8.2 python-editor-1.0.4 pytz-2021.1 pyyaml-5.4.1 querystring-parser-1.2.4 requests-2.26.0 s3transfer-0.5.0 six-1.16.0 smmap-4.0.0 sqlalchemy-1.4.22 sqlparse-0.4.1 tabulate-0.8.9 urllib3-1.26.6 websocket-client-1.1.1
+ apt-get purge -yqq
+ apt-get autoremove -yqq
+ apt-get clean
+ rm -rf /var/lib/apt/lists/auxfiles /var/lib/apt/lists/deb.debian.org_debian_dists_buster-updates_InRelease /var/lib/apt/lists/deb.debian.org_debian_dists_buster-updates_main_binary-amd64_Packages.lz4 /var/lib/apt/lists/deb.debian.org_debian_dists_buster_InRelease /var/lib/apt/lists/deb.debian.org_debian_dists_buster_main_binary-amd64_Packages.lz4 /var/lib/apt/lists/lock /var/lib/apt/lists/partial /var/lib/apt/lists/security.debian.org_debian-security_dists_buster_updates_InRelease /var/lib/apt/lists/security.debian.org_debian-security_dists_buster_updates_main_binary-amd64_Packages.lz4 /tmp/tmpomop0jsxcacert.pem /var/tmp/* /usr/share/man /usr/share/doc /usr/share/doc-base
Removing intermediate container 4fd4341b8164
 ---> 8c5beed37cc3
Step 4/6 : COPY app /app
 ---> 6118c1904c85
Step 5/6 : RUN chmod +x /app/1.sh
 ---> Running in c85f95e57b24
Removing intermediate container c85f95e57b24
 ---> 5619198d3d9c
Step 6/6 : CMD ["/app/1.sh"]
 ---> Running in 6efc5e7f0e2f
Removing intermediate container 6efc5e7f0e2f
 ---> 65dfa9dc0677

Successfully built 65dfa9dc0677
Successfully tagged netology-ml:netology-ml
'netology-ml:netology-ml Dockerfile: netology-ds/HW_1/Dockerfile' has been deployed successfully.
```