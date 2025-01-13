import os

import dotenv
import pyodbc
from py2neo import Graph
from py2neo.bulk import create_nodes, create_relationships
from py2neo.data import Node

# Check if .env exists
if not os.path.isfile(".env"):
	print("Le fichier .env définissant les informations de connexion aux bases de données est manquant.")
	exit(1)

dotenv.load_dotenv()

server = os.environ["TPBDD_SERVER"]
database = os.environ["TPBDD_DB"]
username = os.environ["TPBDD_USERNAME"]
password = os.environ["TPBDD_PASSWORD"]
driver= os.environ["ODBC_DRIVER"]

neo4j_server = os.environ["TPBDD_NEO4J_SERVER"]
neo4j_user = os.environ["TPBDD_NEO4J_USER"]
neo4j_password = os.environ["TPBDD_NEO4J_PASSWORD"]

try:
	print("Test de connexion avec py2neo...", end="", flush=True)
	graph = Graph(neo4j_server, auth=(neo4j_user, neo4j_password))
	graph.run("MATCH (n:Test) RETURN n")
	print("✔️")
except Exception as error:
	print(error)

try:
	print("Test de connexion avec pyodbc...", end="", flush=True)
	with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
		cursor = conn.cursor()
		cursor.execute("SELECT 1")
		print("✔️")
	
except Exception as error:
	print(error)
	print("Causes possibles:")
	print("  - Votre fichier .env est incorrect")
	print("  - Votre fichier .env est vraiment incorrect")

print()
print("L'énoncé et le repository original du TP est disponible sur: https://github.com/lvovan/CS-IMC-TPBDD")
print()
