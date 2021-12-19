create table tokens
(
    address bytea,
    name text,
    symbol text,
    decimals smallint,
    total_supply numeric(78),
    is_erc721 bool
);