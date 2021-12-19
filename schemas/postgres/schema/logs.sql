create table logs
(
    log_index bigint,
    transaction_hash bytea,
    transaction_index bigint,
    address bytea,
    data bytea,
    topic0 bytea,
    topic1 bytea,
    topic2 bytea,
    topic3 bytea,
    block_timestamp timestamptz,
    block_number bigint,
    block_hash bytea
);