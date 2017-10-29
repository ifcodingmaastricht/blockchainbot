CREATE DATABASE cryptocurrencies WITH OWNER = test_username ENCODING = 'UTF8' CONNECTION LIMIT = -1;

CREATE SCHEMA bitcoin AUTHORIZATION test_username;

CREATE TABLE bitcoin.bitfinex
(
    mid double precision,
    bid double precision,
    ask double precision,
    last double precision,
    low double precision,
    high double precision,
    volume double precision,
    "timestamp" "char"
)
WITH (
    OIDS = FALSE
);

ALTER TABLE bitcoin.bitfinex OWNER to test_username;