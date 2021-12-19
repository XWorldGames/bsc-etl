create table traces
(
    transaction_hash bytea,
    transaction_index bigint,
    from_address bytea,
    to_address bytea,
    value numeric(38),
    input bytea,
    output bytea,
    trace_type varchar(16),
    call_type varchar(16),
    reward_type varchar(16),
    gas bigint,
    gas_used bigint,
    subtraces bigint,
    trace_address varchar(8192),
    error text,
    status int,
    block_timestamp timestamptz,
    block_number bigint,
    block_hash bytea,
    trace_id text
);