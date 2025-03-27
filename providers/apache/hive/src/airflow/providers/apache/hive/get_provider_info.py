# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-apache-hive",
        "name": "Apache Hive",
        "description": "`Apache Hive <https://hive.apache.org/>`__\n",
        "state": "ready",
        "source-date-epoch": 1742979243,
        "versions": [
            "9.0.4",
            "9.0.3",
            "9.0.2",
            "9.0.0",
            "8.2.1",
            "8.2.0",
            "8.1.2",
            "8.1.1",
            "8.1.0",
            "8.0.0",
            "7.0.1",
            "7.0.0",
            "6.4.2",
            "6.4.1",
            "6.4.0",
            "6.3.0",
            "6.2.0",
            "6.1.6",
            "6.1.5",
            "6.1.4",
            "6.1.3",
            "6.1.2",
            "6.1.1",
            "6.1.0",
            "6.0.0",
            "5.1.3",
            "5.1.2",
            "5.1.1",
            "5.1.0",
            "5.0.0",
            "4.1.1",
            "4.1.0",
            "4.0.1",
            "4.0.0",
            "3.1.0",
            "3.0.0",
            "2.3.3",
            "2.3.2",
            "2.3.1",
            "2.3.0",
            "2.2.0",
            "2.1.0",
            "2.0.3",
            "2.0.2",
            "2.0.1",
            "2.0.0",
            "1.0.3",
            "1.0.2",
            "1.0.1",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Apache Hive",
                "external-doc-url": "https://hive.apache.org/",
                "how-to-guide": ["/docs/apache-airflow-providers-apache-hive/operators.rst"],
                "logo": "/docs/integration-logos/hive.png",
                "tags": ["apache"],
            }
        ],
        "operators": [
            {
                "integration-name": "Apache Hive",
                "python-modules": [
                    "airflow.providers.apache.hive.operators.hive",
                    "airflow.providers.apache.hive.operators.hive_stats",
                ],
            }
        ],
        "sensors": [
            {
                "integration-name": "Apache Hive",
                "python-modules": [
                    "airflow.providers.apache.hive.sensors.hive_partition",
                    "airflow.providers.apache.hive.sensors.metastore_partition",
                    "airflow.providers.apache.hive.sensors.named_hive_partition",
                ],
            }
        ],
        "hooks": [
            {
                "integration-name": "Apache Hive",
                "python-modules": ["airflow.providers.apache.hive.hooks.hive"],
            }
        ],
        "transfers": [
            {
                "source-integration-name": "Vertica",
                "target-integration-name": "Apache Hive",
                "python-module": "airflow.providers.apache.hive.transfers.vertica_to_hive",
            },
            {
                "source-integration-name": "Apache Hive",
                "target-integration-name": "MySQL",
                "python-module": "airflow.providers.apache.hive.transfers.hive_to_mysql",
            },
            {
                "source-integration-name": "Apache Hive",
                "target-integration-name": "Samba",
                "python-module": "airflow.providers.apache.hive.transfers.hive_to_samba",
            },
            {
                "source-integration-name": "Amazon Simple Storage Service (S3)",
                "target-integration-name": "Apache Hive",
                "python-module": "airflow.providers.apache.hive.transfers.s3_to_hive",
            },
            {
                "source-integration-name": "MySQL",
                "target-integration-name": "Apache Hive",
                "python-module": "airflow.providers.apache.hive.transfers.mysql_to_hive",
            },
            {
                "source-integration-name": "Microsoft SQL Server (MSSQL)",
                "target-integration-name": "Apache Hive",
                "python-module": "airflow.providers.apache.hive.transfers.mssql_to_hive",
            },
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.apache.hive.hooks.hive.HiveCliHook",
                "connection-type": "hive_cli",
            },
            {
                "hook-class-name": "airflow.providers.apache.hive.hooks.hive.HiveServer2Hook",
                "connection-type": "hiveserver2",
            },
            {
                "hook-class-name": "airflow.providers.apache.hive.hooks.hive.HiveMetastoreHook",
                "connection-type": "hive_metastore",
            },
        ],
        "plugins": [
            {"name": "hive", "plugin-class": "airflow.providers.apache.hive.plugins.hive.HivePlugin"}
        ],
        "config": {
            "hive": {
                "description": None,
                "options": {
                    "default_hive_mapred_queue": {
                        "description": "Default mapreduce queue for HiveOperator tasks\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "",
                    },
                    "mapred_job_name_template": {
                        "description": "Template for mapred_job_name in HiveOperator, supports the following named parameters\nhostname, dag_id, task_id, execution_date\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": None,
                    },
                },
            }
        },
        "dependencies": [
            "apache-airflow>=2.9.0",
            "apache-airflow-providers-common-sql>=1.20.0",
            "hmsclient>=0.1.0",
            "pandas>=2.1.2,<2.2",
            "pyhive[hive_pure_sasl]>=0.7.0",
            "thrift>=0.11.0",
            "jmespath>=0.7.0",
        ],
        "optional-dependencies": {
            "amazon": ["apache-airflow-providers-amazon"],
            "microsoft.mssql": ["apache-airflow-providers-microsoft-mssql"],
            "mysql": ["apache-airflow-providers-mysql"],
            "presto": ["apache-airflow-providers-presto"],
            "samba": ["apache-airflow-providers-samba"],
            "vertica": ["apache-airflow-providers-vertica"],
            "common.compat": ["apache-airflow-providers-common-compat"],
        },
        "devel-dependencies": [],
    }
