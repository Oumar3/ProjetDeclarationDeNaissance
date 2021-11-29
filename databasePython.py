import mysql.connector as mc
from datetime import datetime
conf={
    'host':'127.0.0.1',
    'user':'root',
    'password':'66050543OAt@',
    'database':'Declaration_Naissance'
}

connexion=mc.connect(**conf)
cursor=connexion.cursor()
request="insert into infoEnf values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
nom_Enf=input("Entrez le nom de l'enfant : ")
prenom_Enf=input("Entrez le prenom de L'enfant : ")
dateHeurNaissEnf=datetime.now()
lieu_Naiss_Enf=input("Entrez le lieu de naissance de l'enfant : ")
sexe_Enf=input("Entrez le sexe de l'enfant : ")
nom_Pere=input("Entrez le nom de pere : ")
Sit_Matri_Pere=input("Entrez situation matrimonial de pere : ")
fonc_Pere=input("Entrez fonction de pere : ")
date_Naiss_Pere=input("Entrez la date naissance de pere :")
lieu_Naiss_Pere=input("Entrez le lieu de naissance pere : ")
nom_Mere=input("Entrez le nom de mere : ")
Sit_Matri_Mere=input("Entrez situation matrimonial de mere : ")
fonc_Mere=input("Entrez fonction de mere : ")
date_Naiss_Mere=input("Entrez date de naissance de mere : ")
lieu_Naiss_Mere=input("Entrez lieu de naissance de mere : ")

info=(cursor.lastrowid,1,nom_Enf,prenom_Enf,dateHeurNaissEnf,lieu_Naiss_Enf,sexe_Enf,nom_Pere,Sit_Matri_Pere,fonc_Pere,date_Naiss_Pere,lieu_Naiss_Pere,nom_Mere,Sit_Matri_Mere,fonc_Mere,date_Naiss_Mere,lieu_Naiss_Pere)
cursor.execute(request,info)
connexion.commit()

#1980-12-1 23:59:59