create table token_transfers
(
    token_address bytea,
    from_address bytea,
    to_address bytea,
    value numeric(78),
    transaction_hash bytea,
    log_index bigint,
    block_timestamp timestamptz,
    block_number bigint,
    block_hash bytea
);