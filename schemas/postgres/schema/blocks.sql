create table blocks
(
    timestamp timestamptz,
    number bigint,
    hash bytea,
    parent_hash bytea,
    nonce bytea,
    sha3_uncles bytea,
    logs_bloom bytea,
    transactions_root bytea,
    state_root bytea,
    receipts_root bytea,
    miner bytea,
    difficulty numeric(38),
    total_difficulty numeric(38),
    size bigint,
    extra_data bytea,
    gas_limit bigint,
    gas_used bigint,
    transaction_count bigint,
    base_fee_per_gas bigint
);