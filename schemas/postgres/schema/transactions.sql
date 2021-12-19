create table transactions
(
    hash bytea,
    nonce bigint,
    transaction_index bigint,
    from_address bytea,
    to_address bytea,
    value numeric(38),
    gas bigint,
    gas_price bigint,
    input bytea,
    receipt_cumulative_gas_used bigint,
    receipt_gas_used bigint,
    receipt_contract_address bytea,
    receipt_root bytea,
    receipt_status bigint,
    block_timestamp timestamptz,
    block_number bigint,
    block_hash bytea,
    max_fee_per_gas bigint,
    max_priority_fee_per_gas bigint,
    transaction_type bigint,
    receipt_effective_gas_price bigint
);