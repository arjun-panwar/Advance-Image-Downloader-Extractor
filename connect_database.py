from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
#import logger
from logger import App_Logger
import os

class cassandra:
    """
    It is used for connect with Casandra DB

    Parameters
    ----------
    keyspace: name of current keyspace
    """

    def __init__(self, keyspace):
        self.logger = App_Logger("static/imagescrapper.log")  # creating App_Logger object
        cloud_config = {"secure_connect_bundle": "secure-connect-image-scrapper.zip"}
        auth_provider = PlainTextAuthProvider(os.environ['CASSANDRA_USERNAME'], os.environ['CASSANDRA_PASSWORD'])
        self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = self.cluster.connect(keyspace)
        row = self.session.execute("select release_version from system.local").one()
        if row:
            self.logger.log("info", "Cassandra DB- connected" + row[0])  # logging
        else:
            self.logger.log("error", "Cassandra DB- connection error")  # logging

    def create_table(self, table, columns_with_datatype):
        """
        To create table

        Parameters
        ----------
        table:table name
        columns_with_datatype: columns name with datatypes as string
        """
        try:
            qry = f"""
            create table {table} ({columns_with_datatype});
            """
            self.session.execute(qry)
            self.logger.log(
                "info",
                f"Cassandra DB- table created--Name={table}, columns={columns_with_datatype} ",
            )
            return True
        except Exception as e:
            self.logger.log("error", f"Cassandra DB-create table error--{str(e)}")
            return False

    def insert(self, table, columns, values):
        """
        To insert in table

        Parameters
        ----------
        table:table name
        columns: columns name
        values: values
        """
        try:
            qry = f"""
            insert into {table} ({columns}) values ({values});
             """
            self.session.execute(qry)
            self.logger.log(
                "info",
                f"Cassandra DB- data inserted -- Table={table}, columns={columns},values={values} ",
            )
            return True
        except Exception as e:
            self.logger.log("error", f"Cassandra DB-data insert error--{str(e)}")
            return False

    def select(self, table, columns, where=""):
        """
        To select row in table

        Parameters
        ----------
        table:table name
        columns: columns name
        where: where condition
        """
        try:
            if where == "":
                qry = f"""
                     select {columns} from {table} ALLOW FILTERING;
                      """
            else:
                qry = f"""
                    select {columns} from {table} where {where} ALLOW FILTERING;
                    """

            rows = self.session.execute(qry)
            self.logger.log("info", f"Cassandra DB- data selected")
            return rows
        except Exception as e:
            self.logger.log("error", f"Cassandra DB-data selection error--{str(e)}")
            return False

    def update(self, table, columns_with_values, where):
        """
        To update row in table

        Parameters
        ----------
        table:table name
        columns_with_values: columns name with values eg age=88
        where: where condition
        """
        try:
            qry = f"""
            update {table} set {columns_with_values} where {where};
             """
            self.session.execute(qry)
            self.logger.log(
                "info",
                f"Cassandra DB- data updated -- Table={table}, columns={columns_with_values}, where={where} ",
            )
            return True
        except Exception as e:
            self.logger.log("error", f"Cassandra DB-data updating error--{str(e)}")
            return False

    def delete(self, table, where):
        """
        To delete row in table

        Parameters
        ----------
        table:table name
        where: where condition
        """
        try:
            qry = f"""
            delete from {table} where {where};
             """
            self.session.execute(qry)
            self.logger.log(
                "info", f"Cassandra DB- data deleted-- Table={table}, where={where} "
            )
            return True
        except Exception as e:
            self.logger.log("error", f"Cassandra DB-data deleting error--{str(e)}")
            return False

    def execute(self, query):
        """
        To execute any Cassandra query

        Parameters
        ----------
        query:Cassandra query
        """
        try:

            self.session.execute(query)
            return self.logger.log(
                "info", f"Cassandra Query executed successfully - Query={query}"
            )
        except Exception as e:
            self.logger.log(
                "error", f"Cassandra Query not executed - Query={query} error--{str(e)}"
            )
            return False


