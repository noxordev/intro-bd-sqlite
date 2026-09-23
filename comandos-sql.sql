/*seleccionar todos los registros de una tabla*/
select * FROM persona;
/*seleccionar solo algunos campos de una tabla*/
SELECT name, lastname FROM persona;
/*insertar nuevos registros en la tabla*/
INSERT INTO persona(name,lastname,dni,email) VALUES ("Carelos","Betaencourt","983749832Y","cb@gmaiel.com");
/*actualizar registros de la tabla*/
UPDATE persona SET name="Vick", lastname="Arroyo",dni="283298G", email="noxus@mail.com" WHERE id=1;
/*seleccionar*/
SELECT * FROM Persona WHERE name LIKE "vi%";
/*ordenar*/
SELECT * FROM persona ORDER by "dni" ASC;
/*borrar. Utilizar siempre el WHERE*/
DELETE FROM Persona WHERE name LIKE "Ca%";