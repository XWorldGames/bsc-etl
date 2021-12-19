alter table token_approvals add constraint token_approvals_pk primary key (transaction_hash, log_index);

create index token_approvals_block_timestamp_index on token_approvals (block_timestamp desc);

create index token_approvals_token_address_block_timestamp_index on token_approvals (token_address, block_timestamp desc);
create index token_approvals_from_address_block_timestamp_index on token_approvals (from_address, block_timestamp desc);
create index token_approvals_to_address_block_timestamp_index on token_approvals (to_address, block_timestamp desc);
