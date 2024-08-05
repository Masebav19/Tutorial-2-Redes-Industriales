from orm import Table,get_table
from Scripts.user_env import env

venv = env()

class mysql_client():
    """ORM: Cliente mysql para realizar CRUD a una base de datos"""
    def __init__(self) -> None:
        pass
    def connect(self):
        """Conexión a la base de datos MySQL"""
        Table.connect(config_dict={
        'host': venv.MYSQL_URL,
        'port': venv.MYSQL_PORT,
        'user': venv.MYSQL_USER,
        'password': venv.MYSQL_PASSWORD,
        'database': venv.MYSQL_DATA_BASE
        })
    def table(self,TableName = venv.MYSQL_TABLE_NAME):
        """Se conecta a la tabla"""
        self.connect()
        self.Table = get_table(TableName)
    def insert_data(self,data={
        "MbType": "",
        "MbAdd": "0",
        "MbValue": 0
    }):
        """Inserta el dato en la base de datos en función de dos atributos: MbType y MbValue"""
        self.table()
        newData = self.Table(MbType= data["MbType"],MbAdd=data["MbAdd"],MbValue=data["MbValue"])
        return newData.save()
    def ReadDB(self,filter={
        "MbType": ""
    }):
        """Lee la base de datos y 
        Devlueve un array donde cada posición es un diccionario {"MbType": Type,"MbValue": Value}"""
        
        try:
            data = self.Table.where(MbType = filter["MbType"])
        except:
            self.table()
            data = self.Table.where(MbType = filter["MbType"])
        return [{"MbType": Data.MbType,
                "MbValue": Data.MbValue} for Data in data]
    def deleteDB(self,filter={"Id":0}):
        try:
            DataToDelete = self.Table.find(filter["Id"])
            DataToDelete.destroy()
        except:
            self.table()
            DataToDelete = self.Table.find(filter["Id"])
            DataToDelete.destroy()