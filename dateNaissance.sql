CREATE TABLE personnel(
    id_personnel integer PRIMARY KEY NOT NULL,
    nom_personnel     varchar(150) NOT NULL,
    prenom_personnel  varchar(150) NOT NULL,
    fonc_personnel     VARCHAR(100) NOT NULL
)

CREATE TABLE infoEnf(
    id_Enf integer PRIMARY KEY NOT NULL,
    id_personnel_fk integer NOT NULL,
    nom_Enf VARCHAR(100) NOT NULL,
    prenom_Enf VARCHAR(100) NOT NULL,
    date_Heur_Naiss_Enf DATETIME NOT NULL,
    lieu_Naiss_Enf VARCHAR(100) NOT NULL,
    sexe_Enf VARCHAR(10) NOT NULL,
    nom_Pere VARCHAR(100) NOT NULL,
    sit_Matri_Pere VARCHAR(100) NOT NULL,
    fonc_Pere VARCHAR(100) NOT NULL,
    date_Naiss_Pere DATE NOT NULL,
    lieu_Naiss_Pere VARCHAR(100) NOT NULL,
    nom_Mere VARCHAR(100) NOT NULL,
    sit_Matri_Mere VARCHAR(100) NOT NULL,
    fonc_Mere VARCHAR(100) NOT NULL,
    date_Naiss_Mere DATE NOT NULL,
    lieu_Naiss_Mere VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_personnel_fk) REFERENCES personnel(id_personnel)
    
    ) ENGINE=InnoDB;
