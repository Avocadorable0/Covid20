create user hopital with password '000';
create database hp;
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
\c database user 'mdp'

create sequence patient
increment by 1
start with 1;

create table marary(
    idMarary varchar,
    Nom varchar,
    primary key(idMarary)
);

create table controle(
    idMarary varchar,
    Daty date,
    temperature double precision,
    O2 double precision,
    foreign key (idMarary) references marary (idMarary)
);

insert into marary (idMarary,Nom) values(concat('Pat00', nextval('patient')),'Rabe');

select extract(doy from daty) as "jour",controle.temperature as temperature, controle.o2 as axygene from controle
join marary on marary.idMarary=controle.idMarary
where marary.nom='Rasoa';

select marary.nom as nom, controle.daty as daty, controle.temperature as temperature, controle.o2 as o2 from controle
join marary on marary.idMarary=controle.idMarary

select marary.nom,avg(temperature) from controle
join marary on marary.idMarary=controle.idMarary
where (marary.nom ='Rakoto' marary.nom='Jean',marary.nom='Lucas',marary.nom='Rabe',marary.nom='Charo');

create view detailsMarary as
select marary.nom,controle.* from controle
join marary on marary.idMarary=controle.idMarary;