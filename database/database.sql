-- Database: cryptocurrencies

-- DROP DATABASE cryptocurrencies;

CREATE DATABASE cryptocurrencies WITH OWNER = test_username ENCODING = 'UTF8' CONNECTION LIMIT = -1;



-- Schema: bitcoin

-- DROP SCHEMA bitcoin;

CREATE SCHEMA bitcoin AUTHORIZATION test_username;



-- Table: bitcoin.accounts

-- DROP TABLE bitcoin.bitfinex;

CREATE TABLE bitcoin.bitfinex
(
    mid double precision,
    bid double precision,
    ask double precision,
    last double precision,
    low double precision,
    high double precision,
    volume double precision,
    timestamp character varying
)
WITH (
    OIDS = FALSE
);

ALTER TABLE bitcoin.bitfinex OWNER to test_username;



-- Table: bitcoin.accounts

-- DROP TABLE bitcoin.accounts;

CREATE TABLE bitcoin.accounts
(
    balance_bitcoins character varying,
    balance_fiat character varying,
    password character varying,
    id serial primary key
)
WITH (
    OIDS = FALSE
);

ALTER TABLE bitcoin.accounts
    OWNER to test_username;
